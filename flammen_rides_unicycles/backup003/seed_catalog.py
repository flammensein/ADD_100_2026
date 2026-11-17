"""Create and seed the MySQL product catalog from dictionaries.py."""

from __future__ import annotations

import argparse
import os
import re
import unicodedata
from decimal import Decimal
from pathlib import Path
from typing import Any

if __package__:
    from .dictionaries import (
        AVAILABLE_RIM_COLORS,
        BRAKE_OPTIONS,
        CLAMP_COLORS,
        CLAMP_STYLES,
        CRANK_OPTIONS,
        PEDAL_OPTIONS,
        RIM_OPTIONS,
        SADDLE_CUSHION_COLORS,
        SADDLE_LEATHER_COLORS,
        SADDLE_OPTIONS,
        SEAT_POST_OPTIONS,
        TIRE_OPTIONS,
        UNICYCLE_BRANDS,
    )
else:
    from dictionaries import (
        AVAILABLE_RIM_COLORS,
        BRAKE_OPTIONS,
        CLAMP_COLORS,
        CLAMP_STYLES,
        CRANK_OPTIONS,
        PEDAL_OPTIONS,
        RIM_OPTIONS,
        SADDLE_CUSHION_COLORS,
        SADDLE_LEATHER_COLORS,
        SADDLE_OPTIONS,
        SEAT_POST_OPTIONS,
        TIRE_OPTIONS,
        UNICYCLE_BRANDS,
    )


CANONICAL_BRANDS = {
    "bengal": "Bengal",
    "club": "Club",
    "duro": "Duro",
    "hope": "Hope",
    "impact": "Impact",
    "kris_holm": "Kris Holm",
    "mad4one": "Mad4One",
    "magura": "Magura",
    "maxxis": "Maxxis",
    "nimbus": "Nimbus",
    "qu_ax": "Qu-Ax",
    "schwalbe": "Schwalbe",
    "shimano": "Shimano",
    "sram": "SRAM",
    "tektro": "Tektro",
    "wellgo": "Wellgo",
}

SOURCE_BRAND_KEYS = {
    "Bengal": "bengal",
    "Club": "club",
    "Club Unicycles": "club",
    "Duro": "duro",
    "Hope": "hope",
    "Impact": "impact",
    "Kris Holm": "kris_holm",
    "Kris Holm Unicycles (KHU)": "kris_holm",
    "Mad4One": "mad4one",
    "Magura": "magura",
    "Maxxis": "maxxis",
    "Nimbus": "nimbus",
    "Nimbus Unicycles": "nimbus",
    "Qu-Ax": "qu_ax",
    "Qu-Ax Unicycles": "qu_ax",
    "Schwalbe": "schwalbe",
    "Shimano": "shimano",
    "SRAM": "sram",
    "Tektro": "tektro",
    "Wellgo": "wellgo",
}

RIM_BRAND_LABELS = {
    "KH Trials Rim": "Kris Holm",
    'KH Freeride 24" Rim': "Kris Holm",
    'KH Freeride 27.5" Rim': "Kris Holm",
    'Nimbus Dominator 24" Rim': "Nimbus",
    "Nimbus Dominator Rim": "Nimbus",
    "Nimbus Nightrider Rim": "Nimbus",
    "Qu-Ax DB-X Muni Rim": "Qu-Ax",
}

CATEGORY_NAMES = {
    "brake": "Brake system",
    "crank": "Crank",
    "frame_model": "Unicycle model",
    "pedal": "Pedal",
    "rim": "Rim",
    "saddle": "Saddle",
    "seat_post": "Seat post",
    "tire": "Tire",
}

OPTION_GROUP_NAMES = {
    "clamp_color": "Clamp color",
    "clamp_style": "Clamp style",
    "crank_color": "Crank color",
    "pedal_color": "Pedal color",
    "rim_color": "Rim color",
    "saddle_cushion_color": "Saddle cushion color",
    "saddle_cushion_width": "Saddle cushion width",
    "saddle_leather_color": "Saddle handle leather color",
}

MOUNT_STANDARDS = {
    "pivotal": "Pivotal",
    "standard": "Standard",
}

# Keep these keys unchanged if a source item is renamed. Add an override before
# renaming so an existing database row continues to be updated rather than duplicated.
PRODUCT_SEED_KEY_OVERRIDES: dict[tuple[str, str, str], str] = {}
VARIANT_SEED_KEY_OVERRIDES: dict[tuple[str, str], str] = {}


def _slug(value: str) -> str:
    ascii_value = (
        unicodedata.normalize("NFKD", value)
        .encode("ascii", "ignore")
        .decode("ascii")
        .casefold()
    )
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")
    if not slug:
        raise ValueError(f"Cannot create a seed-key segment from {value!r}.")
    return slug


def _decimal_text(value: Decimal) -> str:
    return format(value.normalize(), "f")


def _parse_wheel_size(label: str) -> Decimal:
    match = re.fullmatch(r'\s*(\d+(?:\.\d+)?)\s*"?\s*', label)
    if match is None:
        raise ValueError(f"Invalid wheel-size label: {label!r}")
    return Decimal(match.group(1))


def _wheel_size_label(diameter: Decimal) -> str:
    return f'{_decimal_text(diameter)}"'


def _parse_tire_size(label: str) -> tuple[Decimal, Decimal]:
    match = re.fullmatch(
        r'\s*(\d+(?:\.\d+)?)\s*x\s*(\d+(?:\.\d+)?)\s*"?\s*',
        label,
        flags=re.IGNORECASE,
    )
    if match is None:
        raise ValueError(f"Invalid tire-size label: {label!r}")
    return Decimal(match.group(1)), Decimal(match.group(2))


def _parse_crank_lengths(label: str) -> tuple[Decimal, ...]:
    values = tuple(Decimal(value) for value in re.findall(r"\d+(?:\.\d+)?", label))
    if not values or "mm" not in label.casefold():
        raise ValueError(f"Invalid crank-length label: {label!r}")
    return values


def _brand_key(source_label: str) -> str:
    try:
        return SOURCE_BRAND_KEYS[source_label]
    except KeyError as error:
        raise ValueError(f"No canonical brand mapping for {source_label!r}.") from error


def _product_seed_key(category: str, brand_key: str, source_identity: str) -> str:
    override = PRODUCT_SEED_KEY_OVERRIDES.get(
        (category, brand_key, source_identity)
    )
    if override is not None:
        return override
    return f"product:{category}:{brand_key}:{_slug(source_identity)}"


def _variant_seed_key(product_seed_key: str, source_identity: str) -> str:
    override = VARIANT_SEED_KEY_OVERRIDES.get(
        (product_seed_key, source_identity)
    )
    if override is not None:
        return override
    return f"variant:{product_seed_key}:{_slug(source_identity)}"


def build_seed_plan() -> dict[str, Any]:
    """Build and validate a database-independent representation of the catalog."""
    plan: dict[str, Any] = {
        "brands": [
            {"seed_key": key, "canonical_name": name}
            for key, name in CANONICAL_BRANDS.items()
        ],
        "aliases": {},
        "categories": [
            {"category_code": code, "category_name": name}
            for code, name in CATEGORY_NAMES.items()
        ],
        "mount_standards": [
            {"standard_code": code, "display_label": label}
            for code, label in MOUNT_STANDARDS.items()
        ],
        "wheel_sizes": {},
        "option_groups": [
            {"option_group_code": code, "group_name": name}
            for code, name in OPTION_GROUP_NAMES.items()
        ],
        "option_values": {},
        "clamp_styles": [],
        "products": [],
    }

    def add_alias(context_code: str, label: str, brand_key: str) -> str:
        alias_key = f"alias:{context_code}:{brand_key}:{_slug(label)}"
        alias = {
            "seed_key": alias_key,
            "brand_key": brand_key,
            "context_code": context_code,
            "alias_label": label,
        }
        existing = plan["aliases"].get(alias_key)
        if existing is not None and existing != alias:
            raise ValueError(f"Conflicting source-brand alias {alias_key!r}.")
        plan["aliases"][alias_key] = alias
        return alias_key

    def add_option(group_code: str, value: str) -> None:
        if group_code not in OPTION_GROUP_NAMES:
            raise ValueError(f"Unknown option group {group_code!r}.")
        seed_key = f"option:{group_code}:{_slug(value)}"
        plan["option_values"][seed_key] = {
            "seed_key": seed_key,
            "option_group_code": group_code,
            "value_label": value,
        }

    def add_wheel_size(label: str) -> None:
        diameter = _parse_wheel_size(label)
        canonical_label = _wheel_size_label(diameter)
        plan["wheel_sizes"][_decimal_text(diameter)] = {
            "nominal_diameter_in": diameter,
            "display_label": canonical_label,
        }

    def add_product(
        category_code: str,
        source_identity: str,
        product_name: str,
        brand_label: str,
        brand_context: str,
        *,
        specs: dict[str, Any],
        options: dict[str, list[str]] | None = None,
        wheel_sizes: list[str] | None = None,
        compatible_frame_brands: list[str] | None = None,
        variants: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        brand_key = _brand_key(brand_label)
        alias_key = add_alias(brand_context, brand_label, brand_key)
        seed_key = _product_seed_key(category_code, brand_key, source_identity)

        product = {
            "seed_key": seed_key,
            "category_code": category_code,
            "brand_key": brand_key,
            "brand_alias_seed_key": alias_key,
            "product_name": product_name,
            "specs": specs,
            "options": options or {},
            "wheel_sizes": wheel_sizes or [],
            "compatible_frame_brands": compatible_frame_brands or [],
            "variants": variants or [],
        }
        plan["products"].append(product)

        for group_code, values in product["options"].items():
            for value in values:
                add_option(group_code, value)
        for label in product["wheel_sizes"]:
            add_wheel_size(label)
        for variant in product["variants"]:
            variant["seed_key"] = _variant_seed_key(seed_key, variant["source_identity"])
        return product

    def length_variants(
        source_values: list[Any],
        measurement_code: str,
        unit_code: str,
    ) -> list[dict[str, Any]]:
        variants = []
        for source_value in source_values:
            label = str(source_value)
            if unit_code == "mm" and isinstance(source_value, (int, float)):
                measurements = [(measurement_code, 1, Decimal(str(source_value)), unit_code)]
                identity = f"{_decimal_text(Decimal(str(source_value)))}mm"
            else:
                lengths = _parse_crank_lengths(label)
                measurements = [
                    (measurement_code, index, length, unit_code)
                    for index, length in enumerate(lengths, start=1)
                ]
                identity = label
            variants.append(
                {
                    "source_identity": identity,
                    "display_label": label if unit_code != "mm" or isinstance(source_value, str)
                    else f"{label}mm",
                    "measurements": measurements,
                }
            )
        return variants

    for frame_brand, models in UNICYCLE_BRANDS.items():
        for model_name, specs in models.items():
            add_wheel_size(specs["wheel_size"])
            add_product(
                "frame_model",
                model_name,
                model_name,
                frame_brand,
                "frame",
                specs={
                    "wheel_size_label": specs["wheel_size"],
                    "disc_brakes_supported": bool(specs["disc_brakes_supported"]),
                },
            )

    for tire_brand, sizes in TIRE_OPTIONS.items():
        for size_label in sizes:
            diameter, width = _parse_tire_size(size_label)
            wheel_label = _wheel_size_label(diameter)
            source_identity = f"{_decimal_text(diameter)}x{_decimal_text(width)}"
            add_product(
                "tire",
                source_identity,
                f"{tire_brand} {size_label}",
                tire_brand,
                "component",
                specs={"size_label": size_label, "width_in": width},
                wheel_sizes=[wheel_label],
            )

    for saddle_name, specs in SADDLE_OPTIONS.items():
        mount_label = specs["mount_style"]
        mount_code = _slug(mount_label)
        if mount_code not in MOUNT_STANDARDS:
            raise ValueError(f"Unknown saddle mount standard {mount_label!r}.")
        options = {
            "saddle_cushion_width": list(specs["cushion_widths"]),
            "saddle_cushion_color": list(SADDLE_CUSHION_COLORS),
        }
        if specs["handle_leather_option"]:
            options["saddle_leather_color"] = list(SADDLE_LEATHER_COLORS)
        add_product(
            "saddle",
            saddle_name,
            saddle_name,
            specs["brand"],
            "component",
            specs={
                "mount_standard_code": mount_code,
                "handle_leather_option": bool(specs["handle_leather_option"]),
            },
            options=options,
        )

    for post_name, specs in SEAT_POST_OPTIONS.items():
        mount_label = specs["type"]
        mount_code = _slug(mount_label)
        if mount_code not in MOUNT_STANDARDS:
            raise ValueError(f"Unknown seat-post mount standard {mount_label!r}.")
        lengths = specs["lengths_mm"]
        if not lengths:
            raise ValueError(f"Seat post {post_name!r} has no variant lengths.")
        add_product(
            "seat_post",
            post_name,
            post_name,
            specs["brand"],
            "component",
            specs={
                "mount_standard_code": mount_code,
                "diameter_mm": Decimal(str(specs["diameter_mm"])),
            },
            compatible_frame_brands=list(specs["compatible_brands"]),
            variants=length_variants(lengths, "length", "mm"),
        )

    for rim_name, specs in RIM_OPTIONS.items():
        brand_label = RIM_BRAND_LABELS[rim_name]
        add_product(
            "rim",
            rim_name,
            rim_name,
            brand_label,
            "component",
            specs={
                "diameter_in": Decimal(str(specs["diameter_inches"])),
                "construction": specs["construction"],
                "width_mm": (
                    None
                    if specs["width_mm"] is None
                    else Decimal(str(specs["width_mm"]))
                ),
            },
            options={"rim_color": list(AVAILABLE_RIM_COLORS)},
            wheel_sizes=list(specs["compatible_wheel_sizes"]),
        )

    for crank_name, specs in CRANK_OPTIONS.items():
        add_product(
            "crank",
            crank_name,
            crank_name,
            specs["brand"],
            "component",
            specs={"interface_label": specs["interface"]},
            options={"crank_color": list(specs["available_colors"])},
            variants=length_variants(specs["lengths"], "crank_length", "mm"),
        )

    for pedal_brand, specs in PEDAL_OPTIONS.items():
        add_product(
            "pedal",
            pedal_brand,
            pedal_brand,
            pedal_brand,
            "component",
            specs={"material": specs["material"], "pins": specs["pins"]},
            options={"pedal_color": list(specs["available_colors"])},
        )

    for brake_name, specs in BRAKE_OPTIONS.items():
        add_product(
            "brake",
            brake_name,
            brake_name,
            specs["manufacturer"],
            "component",
            specs={"brake_type": specs["type"]},
        )
        supported_rotors = list(specs["supported_rotors_mm"])
        default_rotor = specs["default_rotor_mm"]
        if default_rotor is not None and default_rotor not in supported_rotors:
            raise ValueError(
                f"Default rotor {default_rotor} is not supported by {brake_name!r}."
            )
        plan["products"][-1]["supported_rotors_mm"] = supported_rotors
        plan["products"][-1]["default_rotor_mm"] = default_rotor

    for style_name, specs in CLAMP_STYLES.items():
        add_option("clamp_style", style_name)
        plan["clamp_styles"].append(
            {
                "style_label": style_name,
                "color_customizable": bool(specs["color_customizable"]),
                "colors": list(CLAMP_COLORS) if specs["color_customizable"] else [],
            }
        )
    for color in CLAMP_COLORS:
        add_option("clamp_color", color)

    product_seed_keys = [product["seed_key"] for product in plan["products"]]
    if len(product_seed_keys) != len(set(product_seed_keys)):
        raise ValueError("Catalog contains duplicate product seed keys.")
    variant_seed_keys = [
        variant["seed_key"]
        for product in plan["products"]
        for variant in product["variants"]
    ]
    if len(variant_seed_keys) != len(set(variant_seed_keys)):
        raise ValueError("Catalog contains duplicate variant seed keys.")
    return plan


def _insert_or_update(
    cursor: Any,
    table: str,
    values: dict[str, Any],
    update_columns: tuple[str, ...],
) -> None:
    columns = tuple(values)
    placeholders = ", ".join(["%s"] * len(columns))
    insert_columns = ", ".join(columns)
    updates = ", ".join(f"{column} = %s" for column in update_columns)
    query = (
        f"INSERT INTO {table} ({insert_columns}) VALUES ({placeholders}) "
        f"ON DUPLICATE KEY UPDATE {updates}"
    )
    parameters = tuple(values[column] for column in columns) + tuple(
        values[column] for column in update_columns
    )
    cursor.execute(query, parameters)


def _lookup_id(cursor: Any, table: str, id_column: str, key_column: str, key: Any) -> int:
    cursor.execute(f"SELECT {id_column} FROM {table} WHERE {key_column} = %s", (key,))
    row = cursor.fetchone()
    if row is None:
        raise RuntimeError(f"Could not find {table}.{key_column}={key!r} after upsert.")
    return int(row[0])


def _seed_lookup_tables(cursor: Any, plan: dict[str, Any]) -> dict[str, dict[Any, int]]:
    ids: dict[str, dict[Any, int]] = {
        "brands": {},
        "aliases": {},
        "options": {},
        "wheel_sizes": {},
        "mount_standards": {},
    }

    for brand in plan["brands"]:
        _insert_or_update(
            cursor,
            "brands",
            brand,
            ("canonical_name",),
        )
        ids["brands"][brand["seed_key"]] = _lookup_id(
            cursor, "brands", "brand_id", "seed_key", brand["seed_key"]
        )

    for alias in plan["aliases"].values():
        values = {
            "brand_id": ids["brands"][alias["brand_key"]],
            "seed_key": alias["seed_key"],
            "context_code": alias["context_code"],
            "alias_label": alias["alias_label"],
        }
        _insert_or_update(
            cursor,
            "brand_aliases",
            values,
            ("brand_id", "context_code", "alias_label"),
        )
        ids["aliases"][alias["seed_key"]] = _lookup_id(
            cursor, "brand_aliases", "brand_alias_id", "seed_key", alias["seed_key"]
        )

    for category in plan["categories"]:
        _insert_or_update(
            cursor,
            "product_categories",
            category,
            ("category_name",),
        )

    for group in plan["option_groups"]:
        _insert_or_update(
            cursor,
            "option_groups",
            group,
            ("group_name",),
        )

    for option in plan["option_values"].values():
        _insert_or_update(
            cursor,
            "option_values",
            option,
            ("option_group_code", "value_label"),
        )
        ids["options"][option["seed_key"]] = _lookup_id(
            cursor, "option_values", "option_value_id", "seed_key", option["seed_key"]
        )

    for size in plan["wheel_sizes"].values():
        values = {
            "nominal_diameter_in": size["nominal_diameter_in"],
            "display_label": size["display_label"],
        }
        _insert_or_update(
            cursor,
            "wheel_sizes",
            values,
            ("display_label",),
        )
        ids["wheel_sizes"][size["display_label"]] = _lookup_id(
            cursor,
            "wheel_sizes",
            "wheel_size_id",
            "display_label",
            size["display_label"],
        )

    for standard in plan["mount_standards"]:
        _insert_or_update(
            cursor,
            "mount_standards",
            standard,
            ("display_label",),
        )
        ids["mount_standards"][standard["standard_code"]] = _lookup_id(
            cursor,
            "mount_standards",
            "mount_standard_id",
            "standard_code",
            standard["standard_code"],
        )

    return ids


def _upsert_detail(cursor: Any, table: str, values: dict[str, Any]) -> None:
    columns = tuple(values)
    placeholders = ", ".join(["%s"] * len(columns))
    insert_columns = ", ".join(columns)
    update_columns = columns[1:]
    updates = ", ".join(f"{column} = %s" for column in update_columns)
    query = (
        f"INSERT INTO {table} ({insert_columns}) VALUES ({placeholders}) "
        f"ON DUPLICATE KEY UPDATE {updates}"
    )
    parameters = tuple(values[column] for column in columns) + tuple(
        values[column] for column in update_columns
    )
    cursor.execute(query, parameters)


def _seed_product(cursor: Any, product: dict[str, Any], ids: dict[str, dict[Any, int]]) -> int:
    brand_id = ids["brands"][product["brand_key"]]
    brand_alias_id = ids["aliases"][product["brand_alias_seed_key"]]
    values = {
        "seed_key": product["seed_key"],
        "category_code": product["category_code"],
        "brand_id": brand_id,
        "brand_alias_id": brand_alias_id,
        "product_name": product["product_name"],
        "is_active": True,
    }
    _insert_or_update(
        cursor,
        "products",
        values,
        ("category_code", "brand_id", "brand_alias_id", "product_name", "is_active"),
    )
    product_id = _lookup_id(
        cursor, "products", "product_id", "seed_key", product["seed_key"]
    )

    spec_key = product["category_code"]
    spec_table = {
        "brake": ("brake_specs", ("brake_type",)),
        "crank": ("crank_specs", ("interface_label",)),
        "frame_model": (
            "unicycle_model_specs",
            ("wheel_size_id", "disc_brakes_supported"),
        ),
        "pedal": ("pedal_specs", ("material", "pins")),
        "rim": ("rim_specs", ("diameter_in", "construction", "width_mm")),
        "saddle": (
            "saddle_specs",
            ("mount_standard_id", "handle_leather_option"),
        ),
        "seat_post": ("seat_post_specs", ("mount_standard_id", "diameter_mm")),
        "tire": ("tire_specs", ("size_label", "width_in")),
    }[spec_key]
    detail_values = {"product_id": product_id}
    for column in spec_table[1]:
        if column == "wheel_size_id":
            label = product["specs"]["wheel_size_label"]
            detail_values[column] = ids["wheel_sizes"][_wheel_size_label(_parse_wheel_size(label))]
        elif column == "mount_standard_id":
            detail_values[column] = ids["mount_standards"][
                product["specs"]["mount_standard_code"]
            ]
        else:
            source_column = {
                "brake_type": "brake_type",
                "diameter_in": "diameter_in",
                "disc_brakes_supported": "disc_brakes_supported",
                "handle_leather_option": "handle_leather_option",
                "interface_label": "interface_label",
                "material": "material",
                "pins": "pins",
                "construction": "construction",
                "width_mm": "width_mm",
                "size_label": "size_label",
                "width_in": "width_in",
                "diameter_mm": "diameter_mm",
            }[column]
            detail_values[column] = product["specs"][source_column]
    _upsert_detail(cursor, spec_table[0], detail_values)

    cursor.execute("DELETE FROM product_option_values WHERE product_id = %s", (product_id,))
    for group_code, labels in product["options"].items():
        for label in labels:
            option_key = f"option:{group_code}:{_slug(label)}"
            cursor.execute(
                "INSERT INTO product_option_values (product_id, option_value_id) "
                "VALUES (%s, %s)",
                (product_id, ids["options"][option_key]),
            )

    cursor.execute(
        "DELETE FROM product_wheel_size_compatibility WHERE product_id = %s",
        (product_id,),
    )
    for label in product["wheel_sizes"]:
        canonical_label = _wheel_size_label(_parse_wheel_size(label))
        cursor.execute(
            "INSERT INTO product_wheel_size_compatibility (product_id, wheel_size_id) "
            "VALUES (%s, %s)",
            (product_id, ids["wheel_sizes"][canonical_label]),
        )

    if spec_key == "seat_post":
        cursor.execute(
            "DELETE FROM seat_post_frame_brand_compatibility "
            "WHERE seat_post_product_id = %s",
            (product_id,),
        )
        for source_brand in product["compatible_frame_brands"]:
            frame_brand_key = _brand_key(source_brand)
            cursor.execute(
                "INSERT INTO seat_post_frame_brand_compatibility "
                "(seat_post_product_id, frame_brand_id) VALUES (%s, %s)",
                (product_id, ids["brands"][frame_brand_key]),
            )

    if spec_key == "brake":
        cursor.execute(
            "DELETE FROM brake_rotor_compatibility WHERE brake_product_id = %s",
            (product_id,),
        )
        for rotor_size in product["supported_rotors_mm"]:
            cursor.execute(
                "INSERT INTO brake_rotor_compatibility "
                "(brake_product_id, rotor_diameter_mm, is_default) "
                "VALUES (%s, %s, %s)",
                (
                    product_id,
                    rotor_size,
                    rotor_size == product["default_rotor_mm"],
                ),
            )

    for variant in product["variants"]:
        variant_values = {
            "product_id": product_id,
            "seed_key": variant["seed_key"],
            "display_label": variant["display_label"],
            "is_active": True,
        }
        _insert_or_update(
            cursor,
            "product_variants",
            variant_values,
            ("product_id", "display_label", "is_active"),
        )
        variant_id = _lookup_id(
            cursor,
            "product_variants",
            "variant_id",
            "seed_key",
            variant["seed_key"],
        )
        cursor.execute(
            "DELETE FROM variant_measurements WHERE variant_id = %s",
            (variant_id,),
        )
        for measurement_code, sequence_no, value, unit_code in variant["measurements"]:
            cursor.execute(
                "INSERT INTO variant_measurements "
                "(variant_id, measurement_code, sequence_no, numeric_value, unit_code) "
                "VALUES (%s, %s, %s, %s, %s)",
                (variant_id, measurement_code, sequence_no, value, unit_code),
            )

    return product_id


def seed_catalog(connection: Any, plan: dict[str, Any]) -> None:
    cursor = connection.cursor()
    try:
        connection.start_transaction()
        ids = _seed_lookup_tables(cursor, plan)

        for product in plan["products"]:
            _seed_product(cursor, product, ids)

        for style in plan["clamp_styles"]:
            style_key = f"option:clamp_style:{_slug(style['style_label'])}"
            style_id = ids["options"][style_key]
            _upsert_detail(
                cursor,
                "clamp_style_settings",
                {
                    "option_value_id": style_id,
                    "color_customizable": style["color_customizable"],
                },
            )
            cursor.execute(
                "DELETE FROM clamp_style_color_options "
                "WHERE clamp_style_option_value_id = %s",
                (style_id,),
            )
            for color in style["colors"]:
                color_key = f"option:clamp_color:{_slug(color)}"
                cursor.execute(
                    "INSERT INTO clamp_style_color_options "
                    "(clamp_style_option_value_id, color_option_value_id) "
                    "VALUES (%s, %s)",
                    (style_id, ids["options"][color_key]),
                )

        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


def apply_schema(connection: Any) -> None:
    schema_file = Path(__file__).with_name("catalog_schema.sql")
    statements = [
        statement.strip()
        for statement in schema_file.read_text(encoding="utf-8").split(";")
        if statement.strip()
    ]
    cursor = connection.cursor()
    try:
        for statement in statements:
            cursor.execute(statement)
        connection.commit()
    finally:
        cursor.close()


def _connect_from_environment() -> Any:
    required = ("MYSQL_HOST", "MYSQL_DATABASE", "MYSQL_USER", "MYSQL_PASSWORD")
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise RuntimeError(
            "Missing MySQL environment variables: " + ", ".join(missing)
        )
    try:
        port = int(os.environ.get("MYSQL_PORT", "3306"))
    except ValueError as error:
        raise ValueError("MYSQL_PORT must be an integer.") from error
    if not 1 <= port <= 65535:
        raise ValueError("MYSQL_PORT must be between 1 and 65535.")

    try:
        import mysql.connector
    except ImportError as error:
        raise RuntimeError(
            "MySQL driver is missing; install requirements.txt first."
        ) from error

    connection_args: dict[str, Any] = {
        "host": os.environ["MYSQL_HOST"],
        "port": port,
        "database": os.environ["MYSQL_DATABASE"],
        "user": os.environ["MYSQL_USER"],
        "password": os.environ["MYSQL_PASSWORD"],
        "connection_timeout": 10,
        "ssl_disabled": False,
        "ssl_verify_cert": True,
        "ssl_verify_identity": True,
    }
    ssl_ca = os.environ.get("MYSQL_SSL_CA")
    if ssl_ca:
        connection_args["ssl_ca"] = ssl_ca
    connection = mysql.connector.connect(**connection_args)

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SHOW SESSION STATUS LIKE 'Ssl_cipher'")
        row = cursor.fetchone()
    except Exception:
        connection.close()
        raise
    finally:
        cursor.close()
    if not isinstance(row, dict) or not row.get("Value"):
        connection.close()
        raise ConnectionError("MySQL connection did not negotiate TLS.")
    return connection


def _print_summary(plan: dict[str, Any]) -> None:
    by_category: dict[str, int] = {}
    variant_count = 0
    option_link_count = 0
    wheel_link_count = 0
    seat_post_link_count = 0
    rotor_link_count = 0
    for product in plan["products"]:
        category = product["category_code"]
        by_category[category] = by_category.get(category, 0) + 1
        variant_count += len(product["variants"])
        option_link_count += sum(len(values) for values in product["options"].values())
        wheel_link_count += len(product["wheel_sizes"])
        seat_post_link_count += len(product["compatible_frame_brands"])
        rotor_link_count += len(product.get("supported_rotors_mm", []))

    print("Catalog seed plan:")
    for category, count in sorted(by_category.items()):
        print(f"  {category}: {count} products")
    print(f"  brands: {len(plan['brands'])}")
    print(f"  product variants: {variant_count}")
    print(f"  product option links: {option_link_count}")
    print(f"  wheel-size compatibility links: {wheel_link_count}")
    print(f"  seat-post/frame-brand links: {seat_post_link_count}")
    print(f"  brake/rotor links: {rotor_link_count}")
    print(f"  clamp styles: {len(plan['clamp_styles'])}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and summarize catalog data without connecting to MySQL",
    )
    mode.add_argument(
        "--apply-schema",
        action="store_true",
        help="create missing tables, then seed using the setup/seed account",
    )
    args = parser.parse_args()

    plan = build_seed_plan()
    _print_summary(plan)
    if args.dry_run:
        return

    connection = _connect_from_environment()
    try:
        if args.apply_schema:
            apply_schema(connection)
        seed_catalog(connection, plan)
    finally:
        connection.close()
    print("Catalog seed completed.")


if __name__ == "__main__":
    main()
