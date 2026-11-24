"""
-----------------------------------------------------------------------
ASSIGNMENT 13B: Python Portion of Final
Project: Flammen Rides Unicycles v1.0.0
-----------------------------------------------------------------------
"""

import math

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
    from .pos_defaults import (
        BASE_PRICE,
        EMAIL_PATTERN,
        SHIPPING_METHODS,
        US_STATE_CODES,
        ZIP_CODE_PATTERN,
    )
    from .order_storage import create_order, generate_invoice_number
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
    from pos_defaults import (
        BASE_PRICE,
        EMAIL_PATTERN,
        SHIPPING_METHODS,
        US_STATE_CODES,
        ZIP_CODE_PATTERN,
    )
    from order_storage import create_order, generate_invoice_number


def get_menu_choice(
    prompt_text: str,
    options_list: list,
    option_label=None,
    default=None,
):
    """
    Prompt user to choose from a numbered list.
    Select a default only when the user submits a blank response.
    """
    if not options_list:
        raise ValueError("options_list must not be empty.")

    if option_label is None:
        option_label = lambda item: str(item)

    if default is not None and default not in options_list:
        raise ValueError("default must be one of options_list.")

    # ℹ️ A generic menu preserves mixed option types (text labels and numeric rotor sizes).
    # 💡 Translation: option_label changes display text only; return the original choice.
    # 🧠 Complexity: displaying/checking choices is O(n); indexed selection is O(1).
    while True:
        print(f"\n\t{prompt_text}")
        for index, option in enumerate(options_list, start=1):
            print(f"\t  [{index}] {option_label(option)}")

        default_hint = f" (blank for default: {default})" if default is not None else ""
        choice = input(f"\n\tSelect an option (Enter number){default_hint}: ").strip()

        if choice == "":
            if default is not None:
                print(f"\tℹ️ Blank input; using default: {default}")
                return default
            print("\n\tINVALID SELECTION - Please try again.")
            continue

        # 🛡️ Catch non-numeric menu input so the program doesn't crash
        try:
            choice_number = int(choice)
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
            continue

        if choice_number < 1 or choice_number > len(options_list):
            print("\n\tINVALID SELECTION - Please try again.")
            continue

        # ✅ Return: selected option item from options_list
        return options_list[choice_number - 1]


def get_validated_input(
    prompt_text: str,
    validator=None,
    invalid_message: str = "Invalid input. Please try again.",
    default=None,
    normalize=lambda value: value,
) -> str:
    """Prompt until a nonblank value passes validation; use defaults only for blank input."""
    default_hint = f" (blank for default: {default})" if default is not None else ""
    while True:
        value = input(f"\t{prompt_text}{default_hint}: ").strip()
        if value == "":
            if default is not None:
                print(f"\tℹ️ Blank input; using default: {default}")
                return default
            print("\tA value is required.")
            continue

        normalized_value = normalize(value)
        if validator is None or validator(normalized_value):
            # ✅ Return: normalized_value (str)
            return normalized_value
        print(f"\t{invalid_message}")


def get_text_choice(
    prompt_text: str,
    options_list: list,
    default=None,
) -> str:
    """Prompt for one of a listed set of text options."""
    if not options_list:
        raise ValueError("options_list must not be empty.")
    if default is not None and default not in options_list:
        raise ValueError("default must be one of options_list.")

    print(f"\n\tAvailable Options: {', '.join(options_list)}")
    # 🧠 Complexity: build this lookup in O(n), then match each response in O(1) average.
    # 💡 Translation: casefold input for matching, but return the catalog's original casing.
    canonical_options = {option.casefold(): option for option in options_list}
    # ✅ Return: matched canonical option (str)
    return get_validated_input(
        prompt_text,
        validator=lambda value: value.casefold() in canonical_options,
        invalid_message="INVALID SELECTION - Please choose an available option.",
        default=default,
        normalize=lambda value: canonical_options.get(value.casefold(), value),
    )


def _select_brakes_enabled(brakes_supported: bool) -> bool:
    if not brakes_supported:
        print("\n\tℹ️ Disc brakes are not supported on this beginner frame model.")
        return False

    b_input = get_validated_input(
        "Add Disc Brakes to this configuration? (y/n)",
        validator=lambda value: value in {"y", "n"},
        invalid_message="Please enter 'y' or 'n'.",
        default="y",
        normalize=str.lower,
    )
    return b_input == "y"


def _frame_seatpost_diameter(frame_brand: str, selected_model: str) -> float:
    diameter = UNICYCLE_BRANDS[frame_brand][selected_model].get("seatpost_diameter_mm")
    if (
        isinstance(diameter, bool)
        or not isinstance(diameter, (int, float))
        or not math.isfinite(diameter)
        or diameter <= 0
    ):
        raise ValueError(
            f"Frame {frame_brand} - {selected_model} must have a valid "
            "seatpost_diameter_mm in the catalog."
        )
    return float(diameter)


def model_opts() -> tuple:
    """
    Prompt user for unicycle brand, model, and brake setup preference.
    Return selected frame brand, model, wheel size, and brake preference.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'UNICYCLE MODEL & FRAME SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    available_models = {
        brand: [
            model
            for model in models
            if _compatible_saddles(_frame_seatpost_diameter(brand, model))
        ]
        for brand, models in UNICYCLE_BRANDS.items()
    }
    if any(
        len(available_models[brand]) != len(models)
        for brand, models in UNICYCLE_BRANDS.items()
    ):
        print("\tℹ️ Frames without a compatible seatpost and saddle " "are not shown.")
    brand_names = [brand for brand, models in available_models.items() if models]
    if not brand_names:
        raise ValueError("No frames have a compatible seatpost and saddle.")
    selected_brand = get_menu_choice(
        "Available Unicycle Brands:",
        brand_names,
    )

    models_dict = UNICYCLE_BRANDS.get(selected_brand, {})
    model_names = available_models[selected_brand]
    selected_model = get_menu_choice(
        f"Available Models for {selected_brand}:",
        model_names,
        option_label=lambda model: (
            f"{model} (Wheel Size: {models_dict.get(model, {}).get('wheel_size', '24\"')})"
        ),
    )

    model_spec = models_dict.get(selected_model, {})
    brakes_yn = _select_brakes_enabled(model_spec.get("disc_brakes_supported", True))
    wheel_size = model_spec["wheel_size"]
    # ✅ Return: (selected_brand, selected_model, wheel_size, brakes_yn) (tuple)
    return selected_brand, selected_model, wheel_size, brakes_yn


def _compatible_tires(frame_wheel_size: str) -> dict:
    return {
        brand: matching
        for brand, sizes in TIRE_OPTIONS.items()
        if (
            matching := [
                size for size in sizes if f'{size.split()[0]}"' == frame_wheel_size
            ]
        )
    }


def tire_opts(frame_wheel_size: str) -> str:
    """
    Prompt user for a tire compatible with the selected frame wheel size.
    Return the selected tire's description.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'TIRE SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    # 🧠 Filtering costs O(T + B): check each tire, then remove brands with no matches.
    # 💡 Translation: keep the full catalog label for display after matching its wheel diameter.
    compatible_sizes_by_brand = _compatible_tires(frame_wheel_size)
    if not compatible_sizes_by_brand:
        raise ValueError(f"No tires are available for wheel size {frame_wheel_size}.")

    available_brands = list(compatible_sizes_by_brand)
    selected_brand = get_menu_choice(
        f"Available Tire Brands for {frame_wheel_size}:",
        available_brands,
    )

    available_sizes = compatible_sizes_by_brand[selected_brand]
    selected_tire_size = get_menu_choice(
        f"Available Sizes for {selected_brand}:",
        available_sizes,
    )

    selected_tire = f"{selected_brand} {selected_tire_size}"
    print(f"\n\t✅ Selected Tire: {selected_tire} (Fits {frame_wheel_size} wheel)")
    # ✅ Return: selected_tire (str)
    return selected_tire


def _compatible_seat_posts(
    frame_seatpost_diameter_mm: float, saddle_mount_style: str
) -> list:
    return [
        post_name
        for post_name, specs in SEAT_POST_OPTIONS.items()
        if specs.get("diameter_mm") == frame_seatpost_diameter_mm
        and specs.get("type") == saddle_mount_style
    ]


def _compatible_saddles(frame_seatpost_diameter_mm: float) -> list:
    return [
        name
        for name, specs in SADDLE_OPTIONS.items()
        if _compatible_seat_posts(
            frame_seatpost_diameter_mm, specs.get("mount_style", "Standard")
        )
    ]


def saddle_opts(frame_seatpost_diameter_mm: float | None = None) -> dict:
    """
    Configure saddle model, cushion width, cushion color, and optional handle leather.
    Return saddle details dictionary including mount_style.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'SADDLE SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    saddle_names = list(SADDLE_OPTIONS.keys())
    if frame_seatpost_diameter_mm is not None:
        saddle_names = _compatible_saddles(frame_seatpost_diameter_mm)
        if not saddle_names:
            raise ValueError(
                f"No saddles have a compatible {frame_seatpost_diameter_mm} mm seatpost."
            )
        if len(saddle_names) < len(SADDLE_OPTIONS):
            print(
                "\tℹ️ Saddles without a compatible seatpost for this frame "
                "are not shown."
            )
    selected_saddle_name = get_menu_choice(
        "Available Saddles:",
        saddle_names,
        option_label=lambda name: (
            f"{name} ({SADDLE_OPTIONS.get(name, {}).get('mount_style', 'Standard')} Mount)"
        ),
    )

    saddle_data = SADDLE_OPTIONS.get(selected_saddle_name, {})
    mount_style = saddle_data.get("mount_style", "Standard")
    widths = saddle_data.get("cushion_widths", ["Medium"])

    width_choice = get_text_choice(
        "Select Cushion Width",
        widths,
        default=widths[0],
    )

    cushion_color = get_text_choice(
        "Enter Cushion Color",
        SADDLE_CUSHION_COLORS,
        default="Black",
    )

    leather_color = "N/A"
    if saddle_data.get("handle_leather_option", False):
        enable_leather = get_validated_input(
            "Enable Custom Leather Handle? (y/n)",
            validator=lambda value: value in {"y", "n"},
            invalid_message="Please enter 'y' or 'n'.",
            normalize=str.lower,
        )
        if enable_leather == "y":
            leather_color = get_text_choice(
                "Enter Leather Color",
                SADDLE_LEATHER_COLORS,
                default="Brown",
            )

    # ✅ Return: saddle configuration (dict)
    return {
        "saddle_name": selected_saddle_name,
        "mount_style": mount_style,
        "width": width_choice,
        "cushion_color": cushion_color,
        "leather_color": leather_color,
    }


def seat_post_opts(frame_seatpost_diameter_mm: float, saddle_mount_style: str) -> dict:
    """
    Filter seatposts by frame diameter and saddle mount type (Pivotal vs Standard).
    Configure post length, clamp style, and optional clamp color customization.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'SEATPOST & CLAMP SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    compatible_posts = _compatible_seat_posts(
        frame_seatpost_diameter_mm, saddle_mount_style
    )
    if not compatible_posts:
        raise ValueError(
            f"No seatposts are compatible with frame diameter {frame_seatpost_diameter_mm} mm "
            f"and saddle mount {saddle_mount_style}."
        )

    selected_post_name = get_menu_choice(
        "Compatible Seatposts:",
        compatible_posts,
        option_label=lambda name: (
            f"{name} ({SEAT_POST_OPTIONS.get(name, {}).get('diameter_mm', 25.4)}mm, "
            f"{SEAT_POST_OPTIONS.get(name, {}).get('type', 'Standard')} Mount)"
        ),
    )

    post_info = SEAT_POST_OPTIONS.get(selected_post_name, {})
    available_lengths = post_info.get("lengths_mm", [300])

    print("\n\tAvailable Lengths:")
    for length in available_lengths:
        print(f"\t  - {length}mm")

    selected_length = get_menu_choice(
        "Select Length in mm:",
        available_lengths,
        option_label=lambda length: f"{length}mm",
        default=available_lengths[0],
    )

    clamp_names = list(CLAMP_STYLES.keys())
    selected_clamp = get_menu_choice(
        "Available Clamp Styles:",
        clamp_names,
    )

    clamp_spec = CLAMP_STYLES.get(selected_clamp, {})
    clamp_color = "Standard Black"
    if clamp_spec.get("color_customizable", False):
        clamp_color = get_text_choice(
            "Select Clamp Color",
            CLAMP_COLORS,
            default=CLAMP_COLORS[0],
        )

    # ✅ Return: seatpost and clamp configuration (dict)
    return {
        "post_model": selected_post_name,
        "diameter_mm": post_info.get("diameter_mm"),
        "length_mm": selected_length,
        "clamp_style": selected_clamp,
        "clamp_color": clamp_color,
    }


def _compatible_rims(wheel_size: str) -> list:
    return [
        rim_name
        for rim_name, specs in RIM_OPTIONS.items()
        if wheel_size in specs.get("compatible_wheel_sizes", [])
    ]


def rim_opts(wheel_size: str) -> dict:
    """
    Configure rim model and color filtered by target wheel_size.
    Return a dictionary of selected rim specifications.
    """
    header_title = f"RIM SELECTION ({wheel_size})"
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{header_title:^35}")
    print(f"\t{'=' * 35:^35}")

    # 🧠 One pass over the rim catalog (O(n)) keeps filtering tied to the selected wheel size.
    matching_rims = _compatible_rims(wheel_size)

    if not matching_rims:
        raise ValueError(f"No rims are available for wheel size {wheel_size}.")

    selected_rim_name = get_menu_choice(
        "Available Rims:",
        matching_rims,
        option_label=lambda rim_name: (
            f"{rim_name} — "
            f"{RIM_OPTIONS.get(rim_name, {}).get('construction', 'double-wall')} "
            f"({RIM_OPTIONS.get(rim_name, {}).get('width_mm', 'N/A')}mm)"
        ),
    )

    # 🛡️ Use .get() lookups for safe fallback retrieval if keys are missing
    selected_specs = RIM_OPTIONS.get(selected_rim_name, {})
    final_width = selected_specs.get("width_mm", "Standard")
    final_construction = selected_specs.get("construction", "double-wall")

    selected_color = get_text_choice(
        "Choose Rim Color",
        AVAILABLE_RIM_COLORS,
        default=AVAILABLE_RIM_COLORS[0],
    )

    # ✅ Return: rim configuration (dict)
    return {
        "rim_model": selected_rim_name,
        "rim_color": selected_color,
        "width_mm": final_width,
        "construction": final_construction,
    }


def crank_opts() -> dict:
    """
    Handle crank arm selection, interface checking, length choice, and color customization.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'CRANK ARM SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    crank_names = list(CRANK_OPTIONS.keys())
    selected_crank_name = get_menu_choice(
        "Available Crank Models:",
        crank_names,
        option_label=lambda name: (
            f"{name} ({CRANK_OPTIONS.get(name, {}).get('interface', 'Standard')})"
        ),
    )

    crank_info = CRANK_OPTIONS.get(selected_crank_name, {})
    interface = crank_info.get("interface", "Standard")
    available_lengths = crank_info.get("lengths", ["125mm"])
    colors = crank_info.get("available_colors", ["Black"])

    selected_length = get_menu_choice(
        "Available Lengths:",
        available_lengths,
    )

    color_choice = get_text_choice(
        "Select Crank Color",
        colors,
        default=colors[0],
    )

    # ✅ Return: crank configuration (dict)
    return {
        "crank_model": selected_crank_name,
        "interface": interface,
        "length": selected_length,
        "color": color_choice,
    }


def pedal_opts() -> dict:
    """
    Handle pedal selection, platform materials, pin types, and color choices.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'PEDAL SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    pedal_brands = list(PEDAL_OPTIONS.keys())
    selected_brand = get_menu_choice(
        "Available Pedal Makes:",
        pedal_brands,
        option_label=lambda brand: (
            f"{brand} — {PEDAL_OPTIONS.get(brand, {}).get('material', 'Plastic platform')} "
            f"({PEDAL_OPTIONS.get(brand, {}).get('pins', 'Molded studs')})"
        ),
    )

    pedal_info = PEDAL_OPTIONS.get(selected_brand, {})
    material = pedal_info.get("material", "Plastic platform")
    pins = pedal_info.get("pins", "Molded studs")
    colors = pedal_info.get("available_colors", ["Black"])

    selected_color = get_text_choice(
        "Choose Pedal Color",
        colors,
        default=colors[0],
    )

    # ✅ Return: pedal configuration (dict)
    return {
        "pedal_brand": selected_brand,
        "material": material,
        "pins": pins,
        "color": selected_color,
    }


def brake_opts(brakes_enabled: bool = True) -> dict:
    """
    Handle disc brake system and rotor diameter selection.
    If brakes_enabled is False, return a bypassed configuration.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'BRAKE SYSTEM SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    # ✅ Return: bypassed brake configuration (dict)
    if not brakes_enabled:
        print("\tℹ️ Disc brakes omitted based on frame choice or user preference.")
        return {
            "brakes_installed": False,
            "brake_model": "None",
            "type": "N/A",
            "rotor_diameter_mm": "N/A",
        }

    brake_models = list(BRAKE_OPTIONS.keys())
    selected_brake_name = get_menu_choice(
        "Available Brake Systems:",
        brake_models,
        option_label=lambda model_name: (
            f"{model_name} — "
            f"{BRAKE_OPTIONS.get(model_name, {}).get('manufacturer', 'Generic')} "
            f"({BRAKE_OPTIONS.get(model_name, {}).get('type', 'Standard Disc')})"
        ),
    )

    brake_spec = BRAKE_OPTIONS.get(selected_brake_name, {})
    brake_type = brake_spec.get("type", "Hydraulic Disc")
    supported_rotors = brake_spec.get("supported_rotors_mm", [180])
    default_rotor = brake_spec.get("default_rotor_mm", 180)

    selected_rotor = "N/A"
    if supported_rotors:
        selected_rotor = get_menu_choice(
            "Available Rotor Sizes:",
            supported_rotors,
            option_label=lambda size: f"{size}mm Rotor",
            default=default_rotor,
        )

    # ✅ Return: brake configuration (dict)
    return {
        "brakes_installed": True,
        "brake_model": selected_brake_name,
        "type": brake_type,
        "rotor_diameter_mm": selected_rotor,
    }


def billing_info() -> dict:
    """
    Collect billing details from the user.
    Return a structured dictionary of billing information.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'BILLING INFORMATION':^35}")
    print(f"\t{'=' * 35:^35}")

    full_name = get_validated_input("Full Name")
    email = get_validated_input(
        "Email Address",
        validator=lambda value: EMAIL_PATTERN.fullmatch(value) is not None,
        invalid_message="Enter a valid email address.",
    )
    address = get_validated_input("Street Address")
    city = get_validated_input("City")
    state = get_validated_input(
        "State (2-letter code)",
        validator=lambda value: value in US_STATE_CODES,
        invalid_message="Enter a valid 2-letter U.S. state or DC code.",
        # 💡 Translation: store state codes in canonical uppercase form.
        normalize=str.upper,
    )
    zip_code = get_validated_input(
        "ZIP Code",
        validator=lambda value: ZIP_CODE_PATTERN.fullmatch(value) is not None,
        invalid_message="Enter a 5-digit ZIP Code or ZIP+4 (12345-6789).",
    )
    payment_method = get_text_choice(
        "Payment Method",
        ["Credit Card", "PayPal", "Apple Pay"],
        default="Credit Card",
    )

    # ✅ Return: billing details (dict)
    return {
        "full_name": full_name,
        "email": email,
        "address": address,
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "payment_method": payment_method,
    }


def shipping_info(
    billing_dict=None,
) -> dict:
    """
    Collect shipping destination and shipping speed preference.
    Calculate shipping cost based on the selected method.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'SHIPPING INFORMATION & METHOD':^35}")
    print(f"\t{'=' * 35:^35}")

    same_as_billing = get_validated_input(
        "Is shipping address same as billing address? (y/n)",
        validator=lambda value: value in {"y", "n"},
        invalid_message="Please enter 'y' or 'n'.",
        normalize=str.lower,
    )

    # 💡 Translation: copy the billing address fields to shipping only when requested.
    if same_as_billing == "y" and billing_dict:
        ship_address = {
            "full_name": billing_dict["full_name"],
            "address": billing_dict["address"],
            "city": billing_dict["city"],
            "state": billing_dict["state"],
            "zip_code": billing_dict["zip_code"],
        }
        print("\tℹ️ Using billing address for shipping.")
    else:
        recipient_name = get_validated_input("Recipient Full Name")
        street_address = get_validated_input("Shipping Street Address")
        ship_city = get_validated_input("Shipping City")
        ship_state = get_validated_input(
            "Shipping State (2-letter code)",
            validator=lambda value: value in US_STATE_CODES,
            invalid_message="Enter a valid 2-letter U.S. state or DC code.",
            normalize=str.upper,
        )
        ship_zip = get_validated_input(
            "Shipping ZIP Code",
            validator=lambda value: ZIP_CODE_PATTERN.fullmatch(value) is not None,
            invalid_message="Enter a 5-digit ZIP Code or ZIP+4 (12345-6789).",
        )

        ship_address = {
            "full_name": recipient_name,
            "address": street_address,
            "city": ship_city,
            "state": ship_state,
            "zip_code": ship_zip,
        }

    choice = get_menu_choice(
        "Available Shipping Options:",
        list(SHIPPING_METHODS),
        option_label=lambda key: (
            f"{SHIPPING_METHODS[key]['name']} — "
            f"${SHIPPING_METHODS[key]['cost']:.2f} "
            f"({SHIPPING_METHODS[key]['days']})"
        ),
    )
    selected = SHIPPING_METHODS[choice]

    # ✅ Return: shipping destination and rate details (dict)
    return {
        "destination": ship_address,
        "method_name": selected["name"],
        "shipping_cost": selected["cost"],
        "delivery_estimate": selected["days"],
    }


def format_invoice(
    order_data: dict,
    invoice_num: str,
    subtotal: float,
    tax_amount: float,
    total_cost: float,
) -> str:
    """Return a customer-readable invoice for the selected order."""
    # ℹ️ Order data combines heterogeneous catalog records, so nested values are dynamic.
    saddle = order_data.get("saddle", {})
    seat_post = order_data.get("seat_post", {})
    rim = order_data.get("rim", {})
    cranks = order_data.get("cranks", {})
    pedals = order_data.get("pedals", {})
    brakes = order_data.get("brakes", {})
    shipping = order_data.get("shipping", {})
    destination = shipping.get("destination", {})
    billing = order_data.get("billing", {})
    shipping_cost = shipping.get("shipping_cost", 0.0)

    # 🖨️ Translation: present structured fields as a receipt without changing saved data.
    # ✅ Return: complete, human-readable invoice text (str).
    return "\n".join(
        [
            "",
            "=" * 58,
            f"Invoice ID: {invoice_num}".center(58),
            "FLAMMEN RIDES UNICYCLES".center(58),
            "CUSTOM ORDER INVOICE".center(58),
            "=" * 58,
            f"Customer: {billing.get('full_name', 'N/A')}",
            "",
            "CONFIGURATION",
            f"  Frame / Model:       {order_data.get('selected_model', 'N/A')}",
            f"  Wheel Size:          {order_data.get('wheel_size', 'N/A')}",
            f"  Tire:                {order_data.get('tire', 'N/A')}",
            f"  Rim:                 {rim.get('rim_model', 'N/A')} "
            f"({rim.get('rim_color', 'N/A')})",
            f"  Saddle:              {saddle.get('saddle_name', 'N/A')} "
            f"[{saddle.get('width', 'N/A')}]",
            f"  Seatpost / Clamp:    {seat_post.get('post_model', 'N/A')} / "
            f"{seat_post.get('clamp_style', 'N/A')}",
            f"  Cranks:              {cranks.get('crank_model', 'N/A')} "
            f"({cranks.get('length', 'N/A')})",
            f"  Pedals:              {pedals.get('pedal_brand', 'N/A')} "
            f"({pedals.get('color', 'N/A')})",
            f"  Brakes:              {brakes.get('brake_model', 'N/A')} "
            f"({brakes.get('type', 'N/A')})",
            "",
            "SHIP TO",
            f"  {destination.get('full_name', 'N/A')}",
            f"  {destination.get('address', 'N/A')}",
            f"  {destination.get('city', 'N/A')}, "
            f"{destination.get('state', 'N/A')} "
            f"{destination.get('zip_code', 'N/A')}",
            f"  Shipping: {shipping.get('method_name', 'N/A')} "
            f"(${shipping_cost:.2f})",
            "",
            "TOTALS",
            f"  Subtotal:             ${subtotal:>8.2f}",
            f"  Estimated Tax (8%):   ${tax_amount:>8.2f}",
            f"  Shipping & Handling:  ${shipping_cost:>8.2f}",
            "-" * 58,
            f"  TOTAL DUE:            ${total_cost:>8.2f}",
            "=" * 58,
        ]
    )


def _show_configuration(order_data: dict, brakes_enabled: bool | None = None) -> None:
    """Display selections made so far, including pending edits."""
    print("\n\t--- Configuration selected so far ---")
    if not order_data:
        print("\t  No selections yet.")

    def show_fields(values: dict, indent: str) -> None:
        for key, value in values.items():
            label = key.replace("_", " ").title()
            if isinstance(value, dict):
                print(f"{indent}{label}:")
                show_fields(value, indent + "  ")
            else:
                print(f"{indent}{label}: {value}")

    show_fields(order_data, "\t  ")
    if brakes_enabled is not None:
        print(f"\t  Brakes requested: {'Yes' if brakes_enabled else 'No'}")


def _edit_conflicts(order_data: dict, brakes_enabled: bool) -> list:
    """Find components that must change to match the proposed configuration."""
    frame_brand = order_data["frame_brand"]
    frame_diameter = _frame_seatpost_diameter(frame_brand, order_data["selected_model"])
    wheel_size = order_data["wheel_size"]
    mount_style = order_data["saddle"].get("mount_style", "Standard")
    compatible_tires = _compatible_tires(wheel_size)
    conflicts = []

    if not any(
        order_data["tire"] == f"{brand} {size}"
        for brand, sizes in compatible_tires.items()
        for size in sizes
    ):
        conflicts.append(("Tire", f"the tire does not fit the {wheel_size} wheel"))
    if order_data["rim"]["rim_model"] not in _compatible_rims(wheel_size):
        conflicts.append(("Rim", f"the rim does not fit the {wheel_size} wheel"))

    compatible_posts = _compatible_seat_posts(frame_diameter, mount_style)
    if not compatible_posts:
        conflicts.append(
            (
                "Saddle",
                f"no seatpost matches the {frame_diameter} mm frame and {mount_style} saddle mount",
            )
        )
    elif order_data["seat_post"]["post_model"] not in compatible_posts:
        conflicts.append(
            (
                "Seatpost",
                f"the seatpost does not match the {frame_diameter} mm frame and {mount_style} saddle mount",
            )
        )

    if order_data["brakes"]["brakes_installed"] != brakes_enabled:
        reason = "brakes were enabled" if brakes_enabled else "brakes were disabled"
        conflicts.append(("Brakes", reason))
    return conflicts


def _edit_order_section(order_data: dict, brakes_enabled: bool) -> bool:
    """Edit one section, resolving compatibility conflicts before committing it."""
    sections = [
        "Frame",
        "Tire",
        "Saddle",
        "Seatpost",
        "Rim",
        "Cranks",
        "Pedals",
        "Brakes",
        "Billing",
        "Shipping",
    ]
    section = get_menu_choice("Select a section to edit:", sections)
    proposed = order_data.copy()
    proposed_brakes_enabled = brakes_enabled
    _show_configuration(proposed, proposed_brakes_enabled)

    if section == "Frame":
        frame_brand, selected_model, wheel_size, proposed_brakes_enabled = model_opts()
        proposed.update(
            {
                "frame_brand": frame_brand,
                "selected_model": selected_model,
                "wheel_size": wheel_size,
            }
        )
    elif section == "Tire":
        proposed["tire"] = tire_opts(proposed["wheel_size"])
    elif section == "Saddle":
        proposed["saddle"] = saddle_opts(
            frame_seatpost_diameter_mm=_frame_seatpost_diameter(
                proposed["frame_brand"], proposed["selected_model"]
            )
        )
    elif section == "Seatpost":
        proposed["seat_post"] = seat_post_opts(
            frame_seatpost_diameter_mm=_frame_seatpost_diameter(
                proposed["frame_brand"], proposed["selected_model"]
            ),
            saddle_mount_style=proposed["saddle"].get("mount_style", "Standard"),
        )
    elif section == "Rim":
        proposed["rim"] = rim_opts(proposed["wheel_size"])
    elif section == "Cranks":
        proposed["cranks"] = crank_opts()
    elif section == "Pedals":
        proposed["pedals"] = pedal_opts()
    elif section == "Brakes":
        model_spec = UNICYCLE_BRANDS[proposed["frame_brand"]][
            proposed["selected_model"]
        ]
        proposed_brakes_enabled = _select_brakes_enabled(
            model_spec.get("disc_brakes_supported", True)
        )
        proposed["brakes"] = brake_opts(brakes_enabled=proposed_brakes_enabled)
    elif section == "Billing":
        proposed["billing"] = billing_info()
        print(
            "\tℹ️ Please review shipping after changing billing, "
            "because the shipping address may use the billing address."
        )
        print("\n\tProposed configuration (not yet applied):")
        _show_configuration(proposed, proposed_brakes_enabled)
        proposed["shipping"] = shipping_info(proposed["billing"])
    else:
        proposed["shipping"] = shipping_info(proposed["billing"])

    while True:
        conflicts = _edit_conflicts(proposed, proposed_brakes_enabled)
        if not conflicts:
            order_data.update(proposed)
            return proposed_brakes_enabled

        print("\n\tThis edit requires changes to other sections:")
        for affected, reason in conflicts:
            print(f"\t- {affected}: {reason}.")

        no_options = (
            ("Tire", not _compatible_tires(proposed["wheel_size"])),
            ("Rim", not _compatible_rims(proposed["wheel_size"])),
            (
                "Saddle",
                not _compatible_saddles(
                    _frame_seatpost_diameter(
                        proposed["frame_brand"], proposed["selected_model"]
                    )
                ),
            ),
            ("Brakes", proposed_brakes_enabled and not BRAKE_OPTIONS),
        )
        unavailable = [
            name
            for name, empty in no_options
            if empty and any(affected == name for affected, _ in conflicts)
        ]
        if unavailable:
            print(
                f"\tNo compatible {' and '.join(unavailable)} options are available; "
                "the edit is canceled."
            )
            return brakes_enabled

        resolution = get_menu_choice(
            "Resolve the incompatibilities or cancel this edit?",
            ["Change Affected Sections", "Cancel Edit"],
        )
        if resolution == "Cancel Edit":
            print("\tEdit canceled; the previous configuration is unchanged.")
            return brakes_enabled

        for affected, _ in conflicts:
            print("\n\tProposed configuration (not yet applied):")
            _show_configuration(proposed, proposed_brakes_enabled)
            if affected == "Tire":
                proposed["tire"] = tire_opts(proposed["wheel_size"])
            elif affected == "Rim":
                proposed["rim"] = rim_opts(proposed["wheel_size"])
            elif affected == "Saddle":
                proposed["saddle"] = saddle_opts(
                    frame_seatpost_diameter_mm=_frame_seatpost_diameter(
                        proposed["frame_brand"], proposed["selected_model"]
                    )
                )
            elif affected == "Seatpost":
                proposed["seat_post"] = seat_post_opts(
                    frame_seatpost_diameter_mm=_frame_seatpost_diameter(
                        proposed["frame_brand"], proposed["selected_model"]
                    ),
                    saddle_mount_style=proposed["saddle"].get(
                        "mount_style", "Standard"
                    ),
                )
            elif affected == "Brakes":
                proposed["brakes"] = brake_opts(brakes_enabled=proposed_brakes_enabled)


def final_order(
    order_data: dict,
    brakes_enabled: bool = True,
) -> str:
    """
    Generate a unique order ID and allow editing until the order is submitted or canceled.
    """
    # ℹ️ The order dictionary combines heterogeneous component records and JSON values.
    try:
        invoice_num = generate_invoice_number()
    except (OSError, ValueError) as exc:
        raise RuntimeError(f"Unable to generate an invoice number: {exc}") from exc
    while True:
        shipping = order_data.get("shipping", {})
        shipping_cost = shipping.get("shipping_cost", 0.0)
        tax_rate = 0.08
        subtotal = BASE_PRICE
        tax_amount = subtotal * tax_rate
        total_cost = subtotal + shipping_cost + tax_amount

        print(format_invoice(order_data, invoice_num, subtotal, tax_amount, total_cost))

        choice = get_menu_choice(
            "Order Options:",
            ["1", "2", "3"],
            option_label=lambda option: {
                "1": "Accept / Buy / Submit",
                "2": "Edit Customization",
                "3": "Cancel Order",
            }[option],
        )

        if choice == "1":
            saved_order: dict[str, object] = {"invoice_num": invoice_num}
            saved_order.update(order_data)
            saved_order["financials"] = {
                "subtotal": subtotal,
                "tax_amount": tax_amount,
                "shipping_cost": shipping_cost,
                "total_cost": total_cost,
            }
            try:
                create_order(saved_order)
            except (OSError, ValueError) as exc:
                raise RuntimeError(f"Unable to save the order: {exc}") from exc
            print(f"\n\t🎉 Order {invoice_num} has been successfully submitted!")
            return "SUBMITTED"
        if choice == "2":
            brakes_enabled = _edit_order_section(order_data, brakes_enabled)
            continue

        print("\n\t❌ Order canceled.")
        return "CANCELED"


def main() -> None:
    """
    Execute the unicycle customization and checkout pipeline in sequence.
    """
    order_data: dict = {}

    # 🧠 STEP 1: Select frame & establish wheel_size and brake support
    _show_configuration(order_data)
    frame_brand, selected_model, wheel_size, brakes_enabled = model_opts()
    order_data.update(
        {
            "frame_brand": frame_brand,
            "selected_model": selected_model,
            "wheel_size": wheel_size,
        }
    )

    # 🧠 STEP 2: Select tire filtered by frame wheel_size
    _show_configuration(order_data, brakes_enabled)
    order_data["tire"] = tire_opts(wheel_size)

    # 🧠 STEP 3: Match the seatpost to the frame diameter and saddle mount
    _show_configuration(order_data, brakes_enabled)
    frame_seatpost_diameter_mm = _frame_seatpost_diameter(frame_brand, selected_model)
    saddle_dict = saddle_opts(frame_seatpost_diameter_mm=frame_seatpost_diameter_mm)
    order_data["saddle"] = saddle_dict
    _show_configuration(order_data, brakes_enabled)
    order_data["seat_post"] = seat_post_opts(
        frame_seatpost_diameter_mm=frame_seatpost_diameter_mm,
        saddle_mount_style=saddle_dict.get("mount_style", "Standard"),
    )

    # 🧠 STEP 4: Select rim filtered by frame wheel_size
    _show_configuration(order_data, brakes_enabled)
    order_data["rim"] = rim_opts(wheel_size)

    # 🧠 STEP 5: Configure drivetrain (cranks and pedals)
    _show_configuration(order_data, brakes_enabled)
    order_data["cranks"] = crank_opts()
    _show_configuration(order_data, brakes_enabled)
    order_data["pedals"] = pedal_opts()

    # 🧠 STEP 6: Configure brakes (bypassed if unsupported or declined)
    _show_configuration(order_data, brakes_enabled)
    order_data["brakes"] = brake_opts(brakes_enabled=brakes_enabled)

    # 🧠 STEP 7: Collect billing & shipping (with billing address reuse option)
    _show_configuration(order_data, brakes_enabled)
    billing_dict = billing_info()
    order_data["billing"] = billing_dict
    _show_configuration(order_data, brakes_enabled)
    order_data["shipping"] = shipping_info(billing_dict)

    # 🧠 STEP 8: Review the completed configuration and checkout.
    final_order(order_data, brakes_enabled)


# ▶️ Imports expose functions without starting checkout; direct execution starts the app.
if __name__ == "__main__":
    main()
