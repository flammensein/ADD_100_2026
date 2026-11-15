"""
-----------------------------------------------------------------------
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Flammen Rides Unicycles v0.3.0
-----------------------------------------------------------------------
"""

import re
import random

BASE_PRICE = 450.00

# -----------------------------------------------------------------------
# SYSTEM CONSTANTS & SCHEMAS
# 📌 AI PROMPT used to generate schema data:
# Generate structured constant dictionaries for unicycle customization
# including brands, tires, saddles, seatposts, rims, pedals, cranks, and brakes.
# Created with AI assistance.
# -----------------------------------------------------------------------

# ℹ️ INFO: Unicycle brands, models, and nominal wheel sizes.
UNICYCLE_BRANDS = {
    "Nimbus Unicycles": {
        'Hatchet 27.5" Mountain': {
            "wheel_size": '27.5"',
            "disc_brakes_supported": True,
        },
        'Oracle 24" Mountain': {
            "wheel_size": '24"',
            "disc_brakes_supported": True,
        },
        'Oracle 29" Mountain': {
            "wheel_size": '29"',
            "disc_brakes_supported": True,
        },
        'Oracle 36"': {"wheel_size": '36"', "disc_brakes_supported": True},
    },
    "Kris Holm Unicycles (KHU)": {
        "KH20 Trials": {
            "wheel_size": '20"',
            "disc_brakes_supported": True,
        },
        "KH24 Mountain": {
            "wheel_size": '24"',
            "disc_brakes_supported": True,
        },
        "KH27.5 Mountain": {
            "wheel_size": '27.5"',
            "disc_brakes_supported": True,
        },
        "KH29 Mountain/Road": {
            "wheel_size": '29"',
            "disc_brakes_supported": True,
        },
        "KH36 Road/Touring": {
            "wheel_size": '36"',
            "disc_brakes_supported": True,
        },
    },
    "Qu-Ax Unicycles": {
        'Muni 24" Q-Axle': {
            "wheel_size": '24"',
            "disc_brakes_supported": True,
        },
        'Muni 27.5" Q-Axle': {
            "wheel_size": '27.5"',
            "disc_brakes_supported": True,
        },
        'RGB 29" Cross/Muni': {
            "wheel_size": '29"',
            "disc_brakes_supported": True,
        },
        'Gentleman 36"': {
            "wheel_size": '36"',
            "disc_brakes_supported": True,
        },
    },
    "Mad4One": {
        'URC 24" Muni': {
            "wheel_size": '24"',
            "disc_brakes_supported": True,
        },
        'URC 27.5" Muni': {
            "wheel_size": '27.5"',
            "disc_brakes_supported": True,
        },
        'URC 29" Road/Muni': {
            "wheel_size": '29"',
            "disc_brakes_supported": True,
        },
    },
    "Club Unicycles": {
        'Club 20" Beginner': {
            "wheel_size": '20"',
            "disc_brakes_supported": False,
        },
        'Club 24"': {
            "wheel_size": '24"',
            "disc_brakes_supported": False,
        },
    },
}

# ℹ️ INFO: Tire options grouped by manufacturer.
TIRE_OPTIONS = {
    "Maxxis": ['20 x 2.5"', '24 x 2.4"', '27.5 x 3.0"', '29 x 2.5"'],
    "Nimbus": ['24 x 3.0"', '29 x 3.0"', '36 x 2.25"'],
    "Qu-Ax": ['24 x 3.0"', '27.5 x 2.6"', '36 x 2.25"'],
    "Schwalbe": ['24 x 2.6"', '27.5 x 2.8"', '29 x 2.6"'],
    "Duro": ['24 x 3.0"', '27.5 x 3.25"'],
}

# ℹ️ INFO: Saddle options with mount styles and customization flags.
SADDLE_OPTIONS = {
    "Kris Holm Fusion One": {
        "brand": "Kris Holm",
        "mount_style": "Pivotal",
        "cushion_widths": ["Slim", "Medium"],
        "handle_leather_option": True,
    },
    "Kris Holm Fusion Freeride": {
        "brand": "Kris Holm",
        "mount_style": "Standard",
        "cushion_widths": ["Medium", "Wide"],
        "handle_leather_option": True,
    },
    "Nimbus Air Saddle": {
        "brand": "Nimbus",
        "mount_style": "Standard",
        "cushion_widths": ["Medium", "Wide"],
        "handle_leather_option": False,
    },
    "Nimbus Stadium": {
        "brand": "Nimbus",
        "mount_style": "Standard",
        "cushion_widths": ["Medium"],
        "handle_leather_option": False,
    },
    "Qu-Ax QX Eleven": {
        "brand": "Qu-Ax",
        "mount_style": "Standard",
        "cushion_widths": ["Slim", "Medium"],
        "handle_leather_option": False,
    },
    "Mad4One Handle Saddle": {
        "brand": "Mad4One",
        "mount_style": "Standard",
        "cushion_widths": ["Slim", "Medium", "Wide"],
        "handle_leather_option": False,
    },
    "Impact Naomi": {
        "brand": "Impact",
        "mount_style": "Standard",
        "cushion_widths": ["Slim"],
        "handle_leather_option": True,
    },
    "Club Logo": {
        "brand": "Club",
        "mount_style": "Standard",
        "cushion_widths": ["Medium"],
        "handle_leather_option": False,
    },
}

# ℹ️ INFO: Seatpost specifications and frame brand compatibility.
SEAT_POST_OPTIONS = {
    "KH Forged Fixed Pivotal Seatpost": {
        "brand": "Kris Holm",
        "type": "Pivotal",
        "diameter_mm": 27.2,
        "lengths_mm": [350],
        "compatible_brands": ["Kris Holm Unicycles (KHU)"],
    },
    "KH Adjustable Standard Seatpost": {
        "brand": "Kris Holm",
        "type": "Standard",
        "diameter_mm": 27.2,
        "lengths_mm": [300, 400],
        "compatible_brands": ["Kris Holm Unicycles (KHU)"],
    },
    "Nimbus Standard Aluminum Seatpost": {
        "brand": "Nimbus",
        "type": "Standard",
        "diameter_mm": 25.4,
        "lengths_mm": [200, 300, 400],
        "compatible_brands": [
            "Nimbus Unicycles",
            "Club Unicycles",
            "Qu-Ax Unicycles",
        ],
    },
    "Qu-Ax Gusseted Aluminum Seatpost": {
        "brand": "Qu-Ax",
        "type": "Standard",
        "diameter_mm": 25.4,
        "lengths_mm": [350, 400],
        "compatible_brands": [
            "Qu-Ax Unicycles",
            "Nimbus Unicycles",
            "Club Unicycles",
        ],
    },
    "Mad4One Reinforced Seatpost": {
        "brand": "Mad4One",
        "type": "Standard",
        "diameter_mm": 27.2,
        "lengths_mm": [300, 400],
        "compatible_brands": ["Mad4One", "Kris Holm Unicycles (KHU)"],
    },
}

# ℹ️ INFO: Seatpost clamp styles and color options.
CLAMP_STYLES = {
    "Double Bolt Clamp": {"color_customizable": False},
    "Quick Release Clamp": {"color_customizable": True},
    "Triple Bolt Muni Clamp": {"color_customizable": True},
}

CLAMP_COLORS = ["Black", "Silver", "Red", "Blue", "Gold", "Green", "Orange"]

# ℹ️ INFO: Rim specifications and compatible wheel size tags.
RIM_OPTIONS = {
    "KH Trials Rim": {
        "diameter_inches": 19,
        "construction": "double-wall",
        "width_mm": 47.2,
        "compatible_wheel_sizes": ['20"', '19"'],
    },
    'KH Freeride 24" Rim': {
        "diameter_inches": 24,
        "construction": "double-wall",
        "width_mm": 47.0,
        "compatible_wheel_sizes": ['24"'],
    },
    'KH Freeride 27.5" Rim': {
        "diameter_inches": 27.5,
        "construction": "double-wall",
        "width_mm": 47.0,
        "compatible_wheel_sizes": ['27.5"'],
    },
    'Nimbus Dominator 24" Rim': {
        "diameter_inches": 24,
        "construction": "double-wall",
        "width_mm": 42.0,
        "compatible_wheel_sizes": ['24"'],
    },
    "Nimbus Dominator Rim": {
        "diameter_inches": 29,
        "construction": "double-wall",
        "width_mm": None,
        "compatible_wheel_sizes": ['29"', '27.5"'],
    },
    "Nimbus Nightrider Rim": {
        "diameter_inches": 36,
        "construction": "double-wall",
        "width_mm": 42.0,
        "compatible_wheel_sizes": ['36"'],
    },
    "Qu-Ax DB-X Muni Rim": {
        "diameter_inches": 27.5,
        "construction": "double-wall",
        "width_mm": 45.0,
        "compatible_wheel_sizes": ['24"', '27.5"', '29"'],
    },
}

AVAILABLE_RIM_COLORS = ["Black", "Silver", "Red", "Blue", "Green", "Gold"]
SADDLE_CUSHION_COLORS = ["Black", "Brown", "Red", "Blue", "Green"]
SADDLE_LEATHER_COLORS = ["Black", "Brown", "Red", "Blue"]

US_STATE_CODES = frozenset(
    """
    AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN
    MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA
    WA WV WI WY DC
    """.split()
)
EMAIL_PATTERN = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
ZIP_CODE_PATTERN = re.compile(r"\d{5}(?:-\d{4})?")

# ℹ️ INFO: Drivetrain options (Cranks & Pedals).
CRANK_OPTIONS = {
    "KH Boundary": {
        "brand": "Kris Holm",
        "interface": "Q-Axle micro spline",
        "lengths": ["117/137mm dual hole", "127/150mm dual hole"],
        "available_colors": ["Black", "Silver"],
    },
    "KH Spirit": {
        "brand": "Kris Holm",
        "interface": "ISIS (Supports External Disc Rotor)",
        "lengths": [
            "110/137mm dual hole",
            "127/150mm dual hole",
            "137/165mm dual hole",
        ],
        "available_colors": ["Black"],
    },
    "Nimbus VCX": {
        "brand": "Nimbus",
        "interface": "ISIS / Standard (Supports D'Brake Mount)",
        "lengths": ["100mm", "125mm", "150mm", "165mm"],
        "available_colors": ["Black", "Silver", "Red"],
    },
    "Qu-Ax Q-Axle": {
        "brand": "Qu-Ax",
        "interface": "Q-Axle 24mm Hollow-Axle",
        "lengths": ["125mm", "137mm", "145mm", "160mm"],
        "available_colors": ["Black", "Red", "Blue", "Gold"],
    },
    "Mad4One Agile": {
        "brand": "Mad4One",
        "interface": "ISIS Splined",
        "lengths": ["125mm", "140mm", "150mm"],
        "available_colors": ["Black", "Silver", "Green", "Orange"],
    },
    "Club Steel": {
        "brand": "Club",
        "interface": "Cotterless, square-tapered",
        "lengths": ["114mm", "125mm"],
        "available_colors": ["Black"],
    },
}

PEDAL_OPTIONS = {
    "Wellgo": {
        "material": "Clear polycarbonate platform",
        "pins": "Removable steel pins",
        "available_colors": ["Clear", "Smoke", "Blue", "Red"],
    },
    "Nimbus": {
        "material": "Plastic studded platform",
        "pins": "Molded studs",
        "available_colors": ["Black", "White"],
    },
    "Kris Holm": {
        "material": "Studded plastic platform",
        "pins": "Molded studs",
        "available_colors": ["Black"],
    },
    "Qu-Ax": {
        "material": "CNC Aluminum Muni platform",
        "pins": "Replaceable steel pins",
        "available_colors": ["Black", "Red", "Silver"],
    },
}

# ℹ️ INFO: Disc brake systems and rotor diameter compatibility.
BRAKE_OPTIONS = {
    "Shimano Deore M6100": {
        "manufacturer": "Shimano",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [160, 180, 203],
        "default_rotor_mm": 180,
    },
    "Shimano SLX M7100": {
        "manufacturer": "Shimano",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [160, 180, 203],
        "default_rotor_mm": 180,
    },
    "Shimano Deore XT M8100": {
        "manufacturer": "Shimano",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [160, 180, 203, 220],
        "default_rotor_mm": 203,
    },
    "Magura MT5 (4-Piston)": {
        "manufacturer": "Magura",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [180, 203],
        "default_rotor_mm": 203,
    },
    "Magura MT4": {
        "manufacturer": "Magura",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [160, 180, 203],
        "default_rotor_mm": 180,
    },
    "Tektro HD-M275": {
        "manufacturer": "Tektro",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [160, 180],
        "default_rotor_mm": 160,
    },
    "Hope Tech 4 E4": {
        "manufacturer": "Hope",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [180, 200, 203, 220],
        "default_rotor_mm": 203,
    },
    "Magura HS33": {
        "manufacturer": "Magura",
        "type": "Hydraulic Rim Brake",
        "supported_rotors_mm": [],
        "default_rotor_mm": None,
    },
    "SRAM Level TL": {
        "manufacturer": "SRAM",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [160, 180],
        "default_rotor_mm": 160,
    },
    "Bengal Helix 7.B": {
        "manufacturer": "Bengal",
        "type": "Mechanical Disc",
        "supported_rotors_mm": [160, 180],
        "default_rotor_mm": 180,
    },
}

SHIPPING_METHODS = {
    "1": {"name": "Standard Ground", "cost": 25.00, "days": "3-5 business days"},
    "2": {"name": "Express 2-Day", "cost": 55.00, "days": "2 business days"},
    "3": {"name": "Overnight Freight", "cost": 95.00, "days": "1 business day"},
}


def get_menu_choice(prompt_text, options_list, option_label=None, default=None):
    """
    Prompt user to choose from a numbered list.
    A default is selected only when the user submits a blank response.
    """
    if not options_list:
        raise ValueError("options_list must not be empty.")

    if option_label is None:
        option_label = lambda item: str(item)

    if default is not None and default not in options_list:
        raise ValueError("default must be one of options_list.")

    while True:
        print(f"\n\t{prompt_text}")
        for index, option in enumerate(options_list, start=1):
            print(f"\t  [{index}] {option_label(option)}")

        default_hint = f" (blank for default: {default})" if default is not None else ""
        choice = input(
            f"\n\tSelect an option (Enter number){default_hint}: "
        ).strip()

        if choice == "":
            if default is not None:
                print(f"\tℹ️ Blank input; using default: {default}")
                return default
            print("\n\tINVALID SELECTION - Please try again.")
            continue

        try:
            choice_number = int(choice)
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
            continue

        if choice_number < 1 or choice_number > len(options_list):
            print("\n\tINVALID SELECTION - Please try again.")
            continue

        return options_list[choice_number - 1]


def get_validated_input(
    prompt_text,
    validator=None,
    invalid_message="Invalid input. Please try again.",
    default=None,
    normalize=lambda value: value,
):
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
            return normalized_value
        print(f"\t{invalid_message}")


def get_text_choice(prompt_text, options_list, default=None):
    """Prompt for one of a listed set of text options."""
    if not options_list:
        raise ValueError("options_list must not be empty.")
    if default is not None and default not in options_list:
        raise ValueError("default must be one of options_list.")

    print(f"\n\tAvailable Options: {', '.join(options_list)}")
    canonical_options = {option.casefold(): option for option in options_list}
    return get_validated_input(
        prompt_text,
        validator=lambda value: value.casefold() in canonical_options,
        invalid_message="INVALID SELECTION - Please choose an available option.",
        default=default,
        normalize=lambda value: canonical_options.get(value.casefold(), value),
    )


def model_opts():
    """
    Prompts user for unicycle brand, model, and brake setup preference.
    Returns selected frame brand, model, wheel size, and brake preference.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'UNICYCLE MODEL & FRAME SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    brand_names = list(UNICYCLE_BRANDS.keys())
    selected_brand = get_menu_choice(
        "Available Unicycle Brands:",
        brand_names,
    )

    models_dict = UNICYCLE_BRANDS.get(selected_brand, {})
    model_names = list(models_dict.keys())
    selected_model = get_menu_choice(
        f"Available Models for {selected_brand}:",
        model_names,
        option_label=lambda model: (
            f"{model} (Wheel Size: {models_dict.get(model, {}).get('wheel_size', '24\"')})"
        ),
    )

    model_spec = models_dict.get(selected_model, {})
    brakes_supported = model_spec.get("disc_brakes_supported", True)

    brakes_yn = False
    if brakes_supported:
        b_input = get_validated_input(
            "Add Disc Brakes to this configuration? (y/n)",
            validator=lambda value: value in {"y", "n"},
            invalid_message="Please enter 'y' or 'n'.",
            default="y",
            normalize=str.lower,
        )
        brakes_yn = b_input == "y"
    else:
        print("\n\tℹ️ Disc brakes are not supported on this beginner frame model.")

    wheel_size = model_spec["wheel_size"]
    return selected_brand, selected_model, wheel_size, brakes_yn


def tire_opts(frame_wheel_size):
    """
    Prompts user for a tire compatible with the selected frame wheel size.
    Returns the selected tire's description.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'TIRE SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    compatible_sizes_by_brand = {
        brand: [
            size
            for size in sizes
            if f'{size.split()[0]}"' == frame_wheel_size
        ]
        for brand, sizes in TIRE_OPTIONS.items()
    }
    compatible_sizes_by_brand = {
        brand: sizes for brand, sizes in compatible_sizes_by_brand.items() if sizes
    }
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
    return selected_tire


def saddle_opts():
    """
    Configures saddle model, cushion width, cushion color, and optional handle leather.
    Returns saddle details dictionary including mount_style.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'SADDLE SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    saddle_names = list(SADDLE_OPTIONS.keys())
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

    return {
        "saddle_name": selected_saddle_name,
        "mount_style": mount_style,
        "width": width_choice,
        "cushion_color": cushion_color,
        "leather_color": leather_color,
    }


def seat_post_opts(frame_brand="Nimbus Unicycles", saddle_mount_style="Standard"):
    """
    Filters seat posts by frame brand compatibility and saddle mount type (Pivotal vs Standard).
    Configures post length, clamp style, and optional clamp color customization.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'SEATPOST & CLAMP SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    compatible_posts = []
    for post_name, specs in SEAT_POST_OPTIONS.items():
        post_type = specs.get("type", "Standard")
        brands = specs.get("compatible_brands", [])
        if frame_brand in brands or post_type == saddle_mount_style:
            compatible_posts.append(post_name)

    if not compatible_posts:
        compatible_posts = list(SEAT_POST_OPTIONS.keys())

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

    return {
        "post_model": selected_post_name,
        "diameter_mm": post_info.get("diameter_mm"),
        "length_mm": selected_length,
        "clamp_style": selected_clamp,
        "clamp_color": clamp_color,
    }


def rim_opts(wheel_size):
    """
    Configures rim model and color filtered by target wheel_size.
    Uses resilient .get() lookups for safe data retrieval.
    """
    header_title = f"RIM SELECTION ({wheel_size})"
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{header_title:^35}")
    print(f"\t{'=' * 35:^35}")

    matching_rims = []
    for rim_name, specs in RIM_OPTIONS.items():
        compatible_sizes = specs.get("compatible_wheel_sizes", [])
        if wheel_size in compatible_sizes:
            matching_rims.append(rim_name)

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

    selected_specs = RIM_OPTIONS.get(selected_rim_name, {})
    final_width = selected_specs.get("width_mm", "Standard")
    final_construction = selected_specs.get("construction", "double-wall")

    selected_color = get_text_choice(
        "Choose Rim Color",
        AVAILABLE_RIM_COLORS,
        default=AVAILABLE_RIM_COLORS[0],
    )

    return {
        "rim_model": selected_rim_name,
        "rim_color": selected_color,
        "width_mm": final_width,
        "construction": final_construction,
    }


def crank_opts():
    """
    Handles crank arm selection, interface checking, length choice, and color customization.
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

    return {
        "crank_model": selected_crank_name,
        "interface": interface,
        "length": selected_length,
        "color": color_choice,
    }


def pedal_opts():
    """
    Handles pedal selection, platform materials, pin types, and color choices.
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

    return {
        "pedal_brand": selected_brand,
        "material": material,
        "pins": pins,
        "color": selected_color,
    }


def brake_opts(brakes_enabled=True):
    """
    Handles disc brake system and rotor diameter selection.
    If brakes_enabled is False, gracefully returns a bypassed configuration.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'BRAKE SYSTEM SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

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

    return {
        "brakes_installed": True,
        "brake_model": selected_brake_name,
        "type": brake_type,
        "rotor_diameter_mm": selected_rotor,
    }


def billing_info():
    """
    Collects billing details from the user.
    Returns a structured dictionary of billing information.
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

    return {
        "full_name": full_name,
        "email": email,
        "address": address,
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "payment_method": payment_method,
    }


def shipping_info(billing_dict=None):
    """
    Collects shipping destination and shipping speed preference.
    Calculates shipping cost based on the selected method.
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

    return {
        "destination": ship_address,
        "method_name": selected["name"],
        "shipping_cost": selected["cost"],
        "delivery_estimate": selected["days"],
    }


def final_order(order_data):
    """
    Generates a unique order ID (invoice_num) and displays an itemized receipt.
    Offers 'Accept/Buy/Submit', 'Edit', and 'Cancel' options.
    """
    random_id = random.randint(10000, 99999)
    invoice_num = f"INV-{random_id}"
    invoice_header = f"Invoice ID: {invoice_num}"

    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'FLAMMEN RIDES UNICYCLES':^35}")
    print(f"\t{'ORDER INVOICE':^35}")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{invoice_header:^35}")

    # ℹ️ Resiliently extract sub-component data using .get()
    saddle = order_data.get("saddle", {})
    seat_post = order_data.get("seat_post", {})
    rim = order_data.get("rim", {})
    cranks = order_data.get("cranks", {})
    pedals = order_data.get("pedals", {})
    brakes = order_data.get("brakes", {})
    shipping = order_data.get("shipping", {})
    tire = order_data.get("tire", "N/A")

    shipping_cost = shipping.get("shipping_cost", 25.00)
    tax_rate = 0.08
    subtotal = BASE_PRICE
    tax_amount = subtotal * tax_rate
    total_cost = subtotal + shipping_cost + tax_amount

    print("\n\t--- COMPONENT SUMMARY ---")
    print(
        f"\t  • Frame / Model:          {order_data.get('selected_model', 'Custom Unicycle')}"
    )
    wheel_display = order_data.get("wheel_size", '36"')
    print(f"\t  • Wheel Size:             {wheel_display}")
    print(f"\t  • Tire:                   {tire}")
    print(
        f"\t  • Rim:                    {rim.get('rim_model', 'N/A')} ({rim.get('rim_color', 'Black')})"
    )
    print(
        f"\t  • Saddle:                 {saddle.get('saddle_name', 'N/A')} [{saddle.get('width', 'Medium')}]"
    )
    print(
        f"\t  • Seatpost & Clamp:       {seat_post.get('post_model', 'N/A')} ({seat_post.get('clamp_style', 'Standard')})"
    )
    print(
        f"\t  • Crank Arms:             {cranks.get('crank_model', 'N/A')} ({cranks.get('length', '125mm')})"
    )
    print(
        f"\t  • Pedals:                 {pedals.get('pedal_brand', 'N/A')} ({pedals.get('color', 'Black')})"
    )
    print(
        f"\t  • Brakes:                 {brakes.get('brake_model', 'None')} ({brakes.get('type', 'N/A')})"
    )

    print("\n\t--- SHIPPING DESTINATION ---")
    dest = shipping.get("destination", {})
    print(f"\t  {dest['full_name']}")
    print(
        f"\t  {dest['address']}, {dest['city']}, {dest['state']} {dest['zip_code']}"
    )
    print(
        f"\t  Method: {shipping.get('method_name', 'Standard Ground')} (${shipping_cost:.2f})"
    )

    print("\n\t--- FINANCIAL BREAKDOWN ---")
    print(f"\t  Subtotal:               ${subtotal:>8.2f}")
    print(f"\t  Estimated Tax (8%):     ${tax_amount:>8.2f}")
    print(f"\t  Shipping & Handling:    ${shipping_cost:>8.2f}")
    print(f"\t  -----------------------------------")
    print(f"\t  TOTAL DUE:              ${total_cost:>8.2f}")
    print("\t==========================================================")

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
        print(f"\n\t🎉 Order {invoice_num} has been successfully submitted!")
        return "SUBMITTED"
    if choice == "2":
        print("\n\t🔄 Returning to customizer menu...")
        return "EDIT"

    print("\n\t❌ Order canceled.")
    return "CANCELED"


def main():
    """
    Main system pipeline executing sprint milestones in sequence.
    """
    # ℹ️ Structured State Flag loop pattern to manage application runtime
    program_running = True
    while program_running:
        # 📌 1. Model & Frame Options
        frame_brand, selected_model, wheel_size, brakes_enabled = model_opts()

        # 📌 2. Tire & Wheel Assembly
        selected_tire = tire_opts(wheel_size)

        # 📌 3. Seating Assembly
        saddle_dict = saddle_opts()
        seat_post_dict = seat_post_opts(
            frame_brand=frame_brand,
            saddle_mount_style=saddle_dict.get("mount_style", "Standard"),
        )

        # 📌 4. Rim Assembly
        rim_dict = rim_opts(wheel_size)

        # 📌 5. Drivetrain Assembly
        crank_dict = crank_opts()
        pedal_dict = pedal_opts()

        # 📌 6. Brakes
        brake_dict = brake_opts(brakes_enabled=brakes_enabled)

        # 📌 7. Checkout & Shipping
        billing_dict = billing_info()
        shipping_dict = shipping_info(billing_dict)

        # 📌 Consolidated Order Object
        order_data = {
            "frame_brand": frame_brand,
            "selected_model": selected_model,
            "wheel_size": wheel_size,
            "tire": selected_tire,
            "rim": rim_dict,
            "saddle": saddle_dict,
            "seat_post": seat_post_dict,
            "cranks": crank_dict,
            "pedals": pedal_dict,
            "brakes": brake_dict,
            "billing": billing_dict,
            "shipping": shipping_dict,
        }

        status = final_order(order_data)
        if status != "EDIT":
            program_running = False


main()
