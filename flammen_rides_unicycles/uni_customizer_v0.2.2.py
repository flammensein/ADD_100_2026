"""
-----------------------------------------------------------------------
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Flammen Rides Unicycles v0.2
Developer: Brent T. Marnati
-----------------------------------------------------------------------
"""

import uuid
from datetime import datetime

# -----------------------------------------------------------------------
# SYSTEM CONSTANTS & SCHEMAS
# 📌 AI PROMPT used to generate schema data:
# Generate structured constant dictionaries for unicycle customization
# including brands, tires, saddles, seatposts, rims, pedals, cranks, and brakes.
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


def model_opts():
    """
    Prompts user for unicycle brand, model, and brake setup preference.
    Returns selected frame brand, wheel size, and disc brakes capability flag.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'UNICYCLE MODEL & FRAME SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    # ℹ️ INFO: Display brand selection list
    brand_names = list(UNICYCLE_BRANDS.keys())
    print("\nAvailable Unicycle Brands:")
    for idx, brand in enumerate(brand_names, start=1):
        print(f"  [{idx}] {brand}")

    choice = input("\nSelect Brand (Enter number): ").strip()
    try:
        brand_idx = int(choice) - 1
        selected_brand = brand_names[brand_idx]
    except (ValueError, IndexError):
        selected_brand = brand_names[0]
        print(f"ℹ️ Defaulting brand to: {selected_brand}")

    # ℹ️ INFO: Fetch models for selected brand using .get()
    models_dict = UNICYCLE_BRANDS.get(selected_brand, {})
    model_names = list(models_dict.keys())

    print(f"\nAvailable Models for {selected_brand}:")
    for idx, model in enumerate(model_names, start=1):
        spec = models_dict.get(model, {})
        wheel = spec.get("wheel_size", '24"')
        print(f"  [{idx}] {model} (Wheel Size: {wheel})")

    m_choice = input("\nSelect Model (Enter number): ").strip()
    try:
        m_idx = int(m_choice) - 1
        selected_model = model_names[m_idx]
    except (ValueError, IndexError):
        selected_model = model_names[0]
        print(f"ℹ️ Defaulting model to: {selected_model}")

    model_spec = models_dict.get(selected_model, {})
    brakes_supported = model_spec.get("disc_brakes_supported", True)

    brakes_yn = False
    if brakes_supported:
        b_input = (
            input("\nAdd Disc Brakes to this configuration? (y/n, Default: y): ")
            .strip()
            .lower()
        )
        if b_input != "n":
            brakes_yn = True
    else:
        print("\nℹ️ Disc brakes are not supported on this beginner frame model.")

    return selected_brand, selected_model, brakes_yn


def tire_opts():
    """
    Prompts user for tire brand and size, then extracts nominal wheel_size.
    Returns extracted wheel_size string for rim filtering.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'TIRE SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    available_brands = list(TIRE_OPTIONS.keys())
    print("\nAvailable Tire Brands:")
    for index, brand in enumerate(available_brands, start=1):
        print(f"  [{index}] {brand}")

    brand_choice = input("\nSelect Tire Brand (Enter number): ").strip()
    try:
        brand_idx = int(brand_choice) - 1
        selected_brand = available_brands[brand_idx]
    except (ValueError, IndexError):
        selected_brand = available_brands[0]
        print(f"ℹ️ Defaulting to: {selected_brand}")

    available_sizes = TIRE_OPTIONS.get(selected_brand, [])
    print(f"\nAvailable Sizes for {selected_brand}:")
    for index, size in enumerate(available_sizes, start=1):
        print(f"  [{index}] {size}")

    size_choice = input("\nSelect Tire Size (Enter number): ").strip()
    try:
        size_idx = int(size_choice) - 1
        selected_tire_size = available_sizes[size_idx]
    except (ValueError, IndexError):
        selected_tire_size = available_sizes[0]
        print(f"ℹ️ Defaulting to: {selected_tire_size}")

    # 💡 TIP: Extract core diameter from string (e.g., '36 x 2.25"' -> '36"')
    raw_parts = selected_tire_size.split()
    wheel_size = f'{raw_parts[0]}"'

    print(
        f"\n✅ Selected Tire: {selected_brand} {selected_tire_size} (Extracted Size: {wheel_size})"
    )
    return wheel_size


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
    print("\nAvailable Saddles:")
    for index, name in enumerate(saddle_names, start=1):
        info = SADDLE_OPTIONS.get(name, {})
        mount = info.get("mount_style", "Standard")
        print(f"  [{index}] {name} ({mount} Mount)")

    choice = input("\nSelect Saddle (Enter number): ").strip()
    try:
        idx = int(choice) - 1
        selected_saddle_name = saddle_names[idx]
    except (ValueError, IndexError):
        selected_saddle_name = saddle_names[0]
        print(f"ℹ️ Defaulting to: {selected_saddle_name}")

    saddle_data = SADDLE_OPTIONS.get(selected_saddle_name, {})
    mount_style = saddle_data.get("mount_style", "Standard")
    widths = saddle_data.get("cushion_widths", ["Medium"])

    print(f"\nAvailable Cushion Widths: {', '.join(widths)}")
    width_choice = input("Select Width: ").strip().title()
    if width_choice not in widths:
        width_choice = widths[0]
        print(f"ℹ️ Defaulting width to: {width_choice}")

    cushion_color = (
        input("Enter Cushion Color (Default: Black): ").strip().title() or "Black"
    )

    leather_color = "N/A"
    if saddle_data.get("handle_leather_option", False):
        enable_leather = input("Enable Custom Leather Handle? (y/n): ").strip().lower()
        if enable_leather == "y":
            leather_color = (
                input("Enter Leather Color (Default: Brown): ").strip().title()
                or "Brown"
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
        # ⚠️ WARNING: Fallback if filtering rules exclude all options
        compatible_posts = list(SEAT_POST_OPTIONS.keys())

    print("\nCompatible Seatposts:")
    for index, name in enumerate(compatible_posts, start=1):
        info = SEAT_POST_OPTIONS.get(name, {})
        diameter = info.get("diameter_mm", 25.4)
        post_type = info.get("type", "Standard")
        print(f"  [{index}] {name} ({diameter}mm, {post_type} Mount)")

    choice = input("\nSelect Seatpost (Enter number): ").strip()
    try:
        idx = int(choice) - 1
        selected_post_name = compatible_posts[idx]
    except (ValueError, IndexError):
        selected_post_name = compatible_posts[0]
        print(f"ℹ️ Defaulting to: {selected_post_name}")

    post_info = SEAT_POST_OPTIONS.get(selected_post_name, {})
    available_lengths = post_info.get("lengths_mm", [300])

    print(f"\nAvailable Lengths: {', '.join(str(l) + 'mm' for l in available_lengths)}")
    len_choice = input("Select Length in mm: ").strip()
    try:
        selected_length = int(len_choice)
        if selected_length not in available_lengths:
            selected_length = available_lengths[0]
            print(f"ℹ️ Defaulting length to: {selected_length}mm")
    except ValueError:
        selected_length = available_lengths[0]
        print(f"ℹ️ Defaulting length to: {selected_length}mm")

    clamp_names = list(CLAMP_STYLES.keys())
    print("\nAvailable Clamp Styles:")
    for index, c_name in enumerate(clamp_names, start=1):
        print(f"  [{index}] {c_name}")

    clamp_choice = input("\nSelect Clamp Style (Enter number): ").strip()
    try:
        c_idx = int(clamp_choice) - 1
        selected_clamp = clamp_names[c_idx]
    except (ValueError, IndexError):
        selected_clamp = clamp_names[0]
        print(f"ℹ️ Defaulting clamp to: {selected_clamp}")

    clamp_spec = CLAMP_STYLES.get(selected_clamp, {})
    clamp_color = "Standard Black"
    if clamp_spec.get("color_customizable", False):
        print(f"\nAvailable Clamp Colors: {', '.join(CLAMP_COLORS)}")
        color_input = input("Select Clamp Color: ").strip().title()
        clamp_color = color_input if color_input in CLAMP_COLORS else CLAMP_COLORS[0]

    return {
        "post_model": selected_post_name,
        "diameter_mm": post_info.get("diameter_mm"),
        "length_mm": selected_length,
        "clamp_style": selected_clamp,
        "clamp_color": clamp_color,
    }


def rim_opts(wheel_size='36"'):
    """
    Configures rim model and color filtered by target wheel_size.
    Uses resilient .get() lookups for safe data retrieval.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{f'RIM SELECTION ({wheel_size})':^35}")
    print(f"\t{'=' * 35:^35}")

    matching_rims = []
    for rim_name, specs in RIM_OPTIONS.items():
        compatible_sizes = specs.get("compatible_wheel_sizes", [])
        if wheel_size in compatible_sizes:
            matching_rims.append(rim_name)

    if not matching_rims:
        # ⚠️ WARNING: Safe guard fallback if size isn't explicitly mapped
        matching_rims = list(RIM_OPTIONS.keys())

    print("\nAvailable Rims:")
    for index, rim_name in enumerate(matching_rims, start=1):
        rim_info = RIM_OPTIONS.get(rim_name, {})
        construction = rim_info.get("construction", "double-wall")
        width = rim_info.get("width_mm", "N/A")
        width_str = f"{width}mm" if width else "Standard Width"
        print(f"  [{index}] {rim_name} — {construction} ({width_str})")

    choice = input("\nSelect Rim Model (Enter number): ").strip()
    try:
        choice_idx = int(choice) - 1
        selected_rim_name = matching_rims[choice_idx]
    except (ValueError, IndexError):
        selected_rim_name = matching_rims[0]
        print(f"ℹ️ Defaulting rim to: {selected_rim_name}")

    selected_specs = RIM_OPTIONS.get(selected_rim_name, {})
    final_width = selected_specs.get("width_mm", "Standard")
    final_construction = selected_specs.get("construction", "double-wall")

    print(f"\nAvailable Rim Colors: {', '.join(AVAILABLE_RIM_COLORS)}")
    selected_color = input("Choose Rim Color: ").strip().title()
    if selected_color not in AVAILABLE_RIM_COLORS:
        selected_color = AVAILABLE_RIM_COLORS[0]
        print(f"ℹ️ Defaulting color to: {selected_color}")

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
    print("\nAvailable Crank Models:")
    for index, name in enumerate(crank_names, start=1):
        info = CRANK_OPTIONS.get(name, {})
        interface = info.get("interface", "Standard")
        print(f"  [{index}] {name} ({interface})")

    choice = input("\nSelect Crank Model (Enter number): ").strip()
    try:
        idx = int(choice) - 1
        selected_crank_name = crank_names[idx]
    except (ValueError, IndexError):
        selected_crank_name = crank_names[0]
        print(f"ℹ️ Defaulting crank to: {selected_crank_name}")

    crank_info = CRANK_OPTIONS.get(selected_crank_name, {})
    interface = crank_info.get("interface", "Standard")
    available_lengths = crank_info.get("lengths", ["125mm"])
    colors = crank_info.get("available_colors", ["Black"])

    print(f"\nAvailable Lengths:")
    for index, length in enumerate(available_lengths, start=1):
        print(f"  [{index}] {length}")

    len_choice = input("\nSelect Length (Enter number): ").strip()
    try:
        len_idx = int(len_choice) - 1
        selected_length = available_lengths[len_idx]
    except (ValueError, IndexError):
        selected_length = available_lengths[0]
        print(f"ℹ️ Defaulting length to: {selected_length}")

    print(f"\nAvailable Colors: {', '.join(colors)}")
    color_choice = input("Select Crank Color: ").strip().title()
    if color_choice not in colors:
        color_choice = colors[0]
        print(f"ℹ️ Defaulting color to: {color_choice}")

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
    print("\nAvailable Pedal Makes:")
    for index, brand in enumerate(pedal_brands, start=1):
        info = PEDAL_OPTIONS.get(brand, {})
        material = info.get("material", "Plastic platform")
        pins = info.get("pins", "Molded studs")
        print(f"  [{index}] {brand} — {material} ({pins})")

    choice = input("\nSelect Pedal Make (Enter number): ").strip()
    try:
        idx = int(choice) - 1
        selected_brand = pedal_brands[idx]
    except (ValueError, IndexError):
        selected_brand = pedal_brands[0]
        print(f"ℹ️ Defaulting pedals to: {selected_brand}")

    pedal_info = PEDAL_OPTIONS.get(selected_brand, {})
    material = pedal_info.get("material", "Plastic platform")
    pins = pedal_info.get("pins", "Molded studs")
    colors = pedal_info.get("available_colors", ["Black"])

    print(f"\nAvailable Colors: {', '.join(colors)}")
    selected_color = input("Choose Pedal Color: ").strip().title()
    if selected_color not in colors:
        selected_color = colors[0]
        print(f"ℹ️ Defaulting color to: {selected_color}")

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
        print("ℹ️ Disc brakes omitted based on frame choice or user preference.")
        return {
            "brakes_installed": False,
            "brake_model": "None",
            "type": "N/A",
            "rotor_diameter_mm": "N/A",
        }

    brake_models = list(BRAKE_OPTIONS.keys())
    print("\nAvailable Brake Systems:")
    for index, model_name in enumerate(brake_models, start=1):
        info = BRAKE_OPTIONS.get(model_name, {})
        mfr = info.get("manufacturer", "Generic")
        b_type = info.get("type", "Standard Disc")
        print(f"  [{index}] {model_name} — {mfr} ({b_type})")

    choice = input("\nSelect Brake Model (Enter number): ").strip()
    try:
        idx = int(choice) - 1
        selected_brake_name = brake_models[idx]
    except (ValueError, IndexError):
        selected_brake_name = brake_models[0]
        print(f"ℹ️ Defaulting brake to: {selected_brake_name}")

    brake_spec = BRAKE_OPTIONS.get(selected_brake_name, {})
    brake_type = brake_spec.get("type", "Hydraulic Disc")
    supported_rotors = brake_spec.get("supported_rotors_mm", [180])
    default_rotor = brake_spec.get("default_rotor_mm", 180)

    selected_rotor = "N/A"
    if supported_rotors:
        print(f"\nAvailable Rotor Sizes:")
        for index, size in enumerate(supported_rotors, start=1):
            print(f"  [{index}] {size}mm Rotor")

        rotor_choice = input("\nSelect Rotor Size (Enter number): ").strip()
        try:
            r_idx = int(rotor_choice) - 1
            selected_rotor = supported_rotors[r_idx]
        except (ValueError, IndexError):
            selected_rotor = default_rotor
            print(f"ℹ️ Defaulting rotor size to: {selected_rotor}mm")

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

    full_name = input("Enter Full Name: ").strip() or "Brent Marnati"
    email = input("Enter Email Address: ").strip() or "brent@example.com"
    address = input("Enter Billing Street Address: ").strip() or "123 Unicycle Way"
    city = input("Enter City: ").strip() or "Portland"
    state = input("Enter State (2 letters): ").strip().upper() or "OR"
    zip_code = input("Enter ZIP Code: ").strip() or "97201"

    payment_method = (
        input(
            "Payment Method [Credit Card / PayPal / Apple Pay] (Default: Credit Card): "
        )
        .strip()
        .title()
        or "Credit Card"
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

    same_as_billing = (
        input("Is shipping address same as billing address? (y/n, Default: y): ")
        .strip()
        .lower()
    )

    if same_as_billing != "n" and billing_dict:
        ship_address = {
            "full_name": billing_dict.get("full_name", "Valued Customer"),
            "address": billing_dict.get("address", "123 Main St"),
            "city": billing_dict.get("city", "Portland"),
            "state": billing_dict.get("state", "OR"),
            "zip_code": billing_dict.get("zip_code", "97201"),
        }
        print("ℹ️ Using billing address for shipping.")
    else:
        ship_address = {
            "full_name": input("Recipient Full Name: ").strip() or "Brent Marnati",
            "address": input("Shipping Street Address: ").strip() or "123 Unicycle Way",
            "city": input("City: ").strip() or "Portland",
            "state": input("State: ").strip().upper() or "OR",
            "zip_code": input("ZIP Code: ").strip() or "97201",
        }

    print("\nAvailable Shipping Options:")
    for key, method in SHIPPING_METHODS.items():
        print(f"  [{key}] {method['name']} — ${method['cost']:.2f} ({method['days']})")

    choice = input("\nSelect Shipping Method (Enter number): ").strip()
    selected = SHIPPING_METHODS.get(choice, SHIPPING_METHODS["1"])

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
    timestamp = datetime.now().strftime("%Y%m%d")
    unique_suffix = str(uuid.uuid4())[:4].upper()
    invoice_num = f"INV-{timestamp}-{unique_suffix}"

    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'FLAMMEN RIDES UNICYCLES':^35}")
    print(f"\t{'ORDER INVOICE':^35}")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{f'Invoice ID: {invoice_num}':^35}")

    base_price = 450.00

    # ℹ️ INFO: Resiliently extract sub-component data using .get()
    saddle = order_data.get("saddle", {})
    seat_post = order_data.get("seat_post", {})
    rim = order_data.get("rim", {})
    cranks = order_data.get("cranks", {})
    pedals = order_data.get("pedals", {})
    brakes = order_data.get("brakes", {})
    shipping = order_data.get("shipping", {})

    shipping_cost = shipping.get("shipping_cost", 25.00)
    tax_rate = 0.08
    subtotal = base_price
    tax_amount = subtotal * tax_rate
    total_cost = subtotal + shipping_cost + tax_amount

    print("\n--- COMPONENT SUMMARY ---")
    print(
        f"  • Frame / Model:          {order_data.get('selected_model', 'Custom Unicycle')}"
    )
    print(f"  • Wheel Size:             {order_data.get('wheel_size', '36\"')}")
    print(
        f"  • Rim:                    {rim.get('rim_model', 'N/A')} ({rim.get('rim_color', 'Black')})"
    )
    print(
        f"  • Saddle:                 {saddle.get('saddle_name', 'N/A')} [{saddle.get('width', 'Medium')}]"
    )
    print(
        f"  • Seatpost & Clamp:       {seat_post.get('post_model', 'N/A')} ({seat_post.get('clamp_style', 'Standard')})"
    )
    print(
        f"  • Crank Arms:             {cranks.get('crank_model', 'N/A')} ({cranks.get('length', '125mm')})"
    )
    print(
        f"  • Pedals:                 {pedals.get('pedal_brand', 'N/A')} ({pedals.get('color', 'Black')})"
    )
    print(
        f"  • Brakes:                 {brakes.get('brake_model', 'None')} ({brakes.get('type', 'N/A')})"
    )

    print("\n--- SHIPPING DESTINATION ---")
    dest = shipping.get("destination", {})
    print(f"  {dest.get('full_name', 'Valued Customer')}")
    print(
        f"  {dest.get('address', '123 Main St')}, {dest.get('city', 'Portland')}, {dest.get('state', 'OR')} {dest.get('zip_code', '97201')}"
    )
    print(
        f"  Method: {shipping.get('method_name', 'Standard Ground')} (${shipping_cost:.2f})"
    )

    print("\n--- FINANCIAL BREAKDOWN ---")
    print(f"  Subtotal:               ${subtotal:>8.2f}")
    print(f"  Estimated Tax (8%):     ${tax_amount:>8.2f}")
    print(f"  Shipping & Handling:    ${shipping_cost:>8.2f}")
    print(f"  -----------------------------------")
    print(f"  TOTAL DUE:              ${total_cost:>8.2f}")
    print("==========================================================")

    print("\nOrder Options:")
    print("  [1] Accept / Buy / Submit")
    print("  [2] Edit Customization")
    print("  [3] Cancel Order")

    choice = input("\nSelect choice (1-3): ").strip()

    if choice == "1":
        print(f"\n🎉 Order {invoice_num} has been successfully submitted!")
        return "SUBMITTED"
    elif choice == "2":
        print("\n🔄 Returning to customizer menu...")
        return "EDIT"
    else:
        print("\n❌ Order canceled.")
        return "CANCELED"


def main():
    """
    Main system pipeline executing sprint milestones in sequence.
    """
    # ℹ️ INFO: Structured State Flag loop pattern to manage application runtime
    program_running = True
    while program_running:
        # 1. Model & Frame Options
        frame_brand, selected_model, brakes_enabled = model_opts()

        # 2. Tire & Wheel Assembly
        wheel_size = tire_opts()

        # 3. Seating Assembly
        saddle_dict = saddle_opts()
        seat_post_dict = seat_post_opts(
            frame_brand=frame_brand,
            saddle_mount_style=saddle_dict.get("mount_style", "Standard"),
        )

        # 4. Rim Assembly
        rim_dict = rim_opts(wheel_size)

        # 5. Drivetrain Assembly
        crank_dict = crank_opts()
        pedal_dict = pedal_opts()

        # 6. Brakes
        brake_dict = brake_opts(brakes_enabled=brakes_enabled)

        # 7. Checkout & Shipping
        billing_dict = billing_info()
        shipping_dict = shipping_info(billing_dict)

        # Consolidated Order Object
        order_data = {
            "frame_brand": frame_brand,
            "selected_model": selected_model,
            "wheel_size": wheel_size,
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


if __name__ == "__main__":
    main()
