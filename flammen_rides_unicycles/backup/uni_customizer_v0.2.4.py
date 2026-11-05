"""
-----------------------------------------------------------------------
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Flammen Rides Unicycles v0.2
-----------------------------------------------------------------------
"""

import logging
import random

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)

MAX_SELECTION_ATTEMPTS = 5

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
    Returns selected frame brand, model, and disc brakes capability flag.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'UNICYCLE MODEL & FRAME SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    # ℹ️ Display brand selection list
    brand_names = list(UNICYCLE_BRANDS.keys())
    selected_brand = ""
    attempts = 0
    while not selected_brand:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_brand = brand_names[0]
            print(f"\n\tMaximum attempts reached. Defaulting to: {selected_brand}")
            break
        try:
            print("\n\tAvailable Unicycle Brands:")
            for brand in brand_names:
                print(f"\t  [{brand_names.index(brand) + 1}] {brand}")

            choice = int(input("\n\tSelect Brand (Enter number): ").strip())
            if choice < 1 or choice > len(brand_names):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_brand = brand_names[choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        # ℹ️ Catches EOF Errors if the user presses keyboard exit shortcuts at the input prompt.
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_brand = brand_names[0]
            break
        except Exception:
            logging.exception("Unexpected error during model brand selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    # ℹ️ Fetch models for selected brand using .get()
    models_dict = UNICYCLE_BRANDS.get(selected_brand, {})
    model_names = list(models_dict.keys())
    selected_model = ""
    attempts = 0
    while not selected_model:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_model = model_names[0]
            print(f"\n\tMaximum attempts reached. Defaulting to: {selected_model}")
            break
        try:
            print(f"\n\tAvailable Models for {selected_brand}:")
            for model in model_names:
                spec = models_dict.get(model, {})
                wheel = spec.get("wheel_size", '24"')
                print(
                    f"\t  [{model_names.index(model) + 1}] {model} (Wheel Size: {wheel})"
                )

            m_choice = int(input("\n\tSelect Model (Enter number): ").strip())
            if m_choice < 1 or m_choice > len(model_names):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_model = model_names[m_choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_model = model_names[0]
            break
        except Exception:
            logging.exception("Unexpected error during model selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    model_spec = models_dict.get(selected_model, {})
    brakes_supported = model_spec.get("disc_brakes_supported", True)

    brakes_yn = False
    if brakes_supported:
        b_input = (
            input("\n\tAdd Disc Brakes to this configuration? (y/n, Default: y): ")
            .strip()
            .lower()
        )
        if b_input != "n":
            brakes_yn = True
    else:
        print("\n\tℹ️ Disc brakes are not supported on this beginner frame model.")

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
    selected_brand = ""
    attempts = 0
    while not selected_brand:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_brand = available_brands[0]
            print(f"\n\tMaximum attempts reached. Defaulting to: {selected_brand}")
            break
        try:
            print("\n\tAvailable Tire Brands:")
            for brand in available_brands:
                print(f"\t  [{available_brands.index(brand) + 1}] {brand}")

            brand_choice = int(input("\n\tSelect Tire Brand (Enter number): ").strip())
            if brand_choice < 1 or brand_choice > len(available_brands):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_brand = available_brands[brand_choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_brand = available_brands[0]
            break
        except Exception:
            logging.exception("Unexpected error during tire brand selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    available_sizes = TIRE_OPTIONS.get(selected_brand, [])
    selected_tire_size = ""
    attempts = 0
    while not selected_tire_size:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_tire_size = available_sizes[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_tire_size}"
            )
            break
        try:
            print(f"\n\tAvailable Sizes for {selected_brand}:")
            for size in available_sizes:
                print(f"\t  [{available_sizes.index(size) + 1}] {size}")

            size_choice = int(input("\n\tSelect Tire Size (Enter number): ").strip())
            if size_choice < 1 or size_choice > len(available_sizes):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_tire_size = available_sizes[size_choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_tire_size = available_sizes[0]
            break
        except Exception:
            logging.exception("Unexpected error during tire size selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    # 💡 Extract core diameter from string (e.g., '36 x 2.25"' -> '36"')
    raw_parts = selected_tire_size.split()
    wheel_size = f'{raw_parts[0]}"'

    print(
        f"\n\t✅ Selected Tire: {selected_brand} {selected_tire_size} (Extracted Size: {wheel_size})"
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
    selected_saddle_name = ""
    attempts = 0
    while not selected_saddle_name:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_saddle_name = saddle_names[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_saddle_name}"
            )
            break
        try:
            print("\n\tAvailable Saddles:")
            for name in saddle_names:
                info = SADDLE_OPTIONS.get(name, {})
                mount = info.get("mount_style", "Standard")
                print(f"\t  [{saddle_names.index(name) + 1}] {name} ({mount} Mount)")

            choice = int(input("\n\tSelect Saddle (Enter number): ").strip())
            if choice < 1 or choice > len(saddle_names):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_saddle_name = saddle_names[choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_saddle_name = saddle_names[0]
            break
        except Exception:
            logging.exception("Unexpected error during saddle selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    saddle_data = SADDLE_OPTIONS.get(selected_saddle_name, {})
    mount_style = saddle_data.get("mount_style", "Standard")
    widths = saddle_data.get("cushion_widths", ["Medium"])

    print(f"\n\tAvailable Cushion Widths: {', '.join(widths)}")
    width_choice = input("\tSelect Width: ").strip().title()
    if width_choice not in widths:
        width_choice = widths[0]
        print(f"\tℹ️ Defaulting width to: {width_choice}")

    cushion_color = input("\tEnter Cushion Color (Default: Black): ").strip().title()
    if cushion_color == "":
        cushion_color = "Black"

    leather_color = "N/A"
    if saddle_data.get("handle_leather_option", False):
        enable_leather = (
            input("\tEnable Custom Leather Handle? (y/n): ").strip().lower()
        )
        if enable_leather == "y":
            leather_color = (
                input("\tEnter Leather Color (Default: Brown): ").strip().title()
            )
            if leather_color == "":
                leather_color = "Brown"

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
        # ⚠️ Fallback if filtering rules exclude all options
        compatible_posts = list(SEAT_POST_OPTIONS.keys())

    selected_post_name = ""
    attempts = 0
    while not selected_post_name:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_post_name = compatible_posts[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_post_name}"
            )
            break
        try:
            print("\n\tCompatible Seatposts:")
            for name in compatible_posts:
                info = SEAT_POST_OPTIONS.get(name, {})
                diameter = info.get("diameter_mm", 25.4)
                post_type = info.get("type", "Standard")
                print(
                    f"\t  [{compatible_posts.index(name) + 1}] {name} ({diameter}mm, {post_type} Mount)"
                )

            choice = int(input("\n\tSelect Seatpost (Enter number): ").strip())
            if choice < 1 or choice > len(compatible_posts):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_post_name = compatible_posts[choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_post_name = compatible_posts[0]
            break
        except Exception:
            logging.exception("Unexpected error during seatpost selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    post_info = SEAT_POST_OPTIONS.get(selected_post_name, {})
    available_lengths = post_info.get("lengths_mm", [300])

    # ℹ️ Build list of formatted length strings using a standard for loop
    print("\n\tAvailable Lengths:")
    for length in available_lengths:
        print(f"\t  - {length}mm")

    len_choice = input("\tSelect Length in mm: ").strip()
    try:
        selected_length = int(len_choice)
        if selected_length not in available_lengths:
            selected_length = available_lengths[0]
            print(f"\tℹ️ Defaulting length to: {selected_length}mm")
    except ValueError:
        selected_length = available_lengths[0]
        print(f"\tℹ️ Defaulting length to: {selected_length}mm")

    clamp_names = list(CLAMP_STYLES.keys())
    selected_clamp = ""
    attempts = 0
    while not selected_clamp:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_clamp = clamp_names[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_clamp}"
            )
            break
        try:
            print("\n\tAvailable Clamp Styles:")
            for c_name in clamp_names:
                print(f"\t  [{clamp_names.index(c_name) + 1}] {c_name}")

            clamp_choice = int(input("\n\tSelect Clamp Style (Enter number): ").strip())
            if clamp_choice < 1 or clamp_choice > len(clamp_names):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_clamp = clamp_names[clamp_choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_clamp = clamp_names[0]
            break
        except Exception:
            logging.exception("Unexpected error during clamp selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    clamp_spec = CLAMP_STYLES.get(selected_clamp, {})
    clamp_color = "Standard Black"
    if clamp_spec.get("color_customizable", False):
        print(f"\n\tAvailable Clamp Colors: {', '.join(CLAMP_COLORS)}")
        color_input = input("\tSelect Clamp Color: ").strip().title()
        if color_input in CLAMP_COLORS:
            clamp_color = color_input
        else:
            clamp_color = CLAMP_COLORS[0]
            print(f"\tℹ️ Defaulting clamp color to: {clamp_color}")

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
        # ⚠️ Safe guard fallback if size isn't explicitly mapped
        matching_rims = list(RIM_OPTIONS.keys())

    selected_rim_name = ""
    attempts = 0
    while not selected_rim_name:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_rim_name = matching_rims[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_rim_name}"
            )
            break
        try:
            print("\n\tAvailable Rims:")
            for rim_name in matching_rims:
                rim_info = RIM_OPTIONS.get(rim_name, {})
                construction = rim_info.get("construction", "double-wall")
                width = rim_info.get("width_mm", "N/A")
                if width:
                    width_str = f"{width}mm"
                else:
                    width_str = "Standard Width"
                print(
                    f"\t  [{matching_rims.index(rim_name) + 1}] {rim_name} — {construction} ({width_str})"
                )

            choice = int(input("\n\tSelect Rim Model (Enter number): ").strip())
            if choice < 1 or choice > len(matching_rims):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_rim_name = matching_rims[choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_rim_name = matching_rims[0]
            break
        except Exception:
            logging.exception("Unexpected error during rim selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    selected_specs = RIM_OPTIONS.get(selected_rim_name, {})
    final_width = selected_specs.get("width_mm", "Standard")
    final_construction = selected_specs.get("construction", "double-wall")

    print(f"\n\tAvailable Rim Colors: {', '.join(AVAILABLE_RIM_COLORS)}")
    selected_color = input("\tChoose Rim Color: ").strip().title()
    if selected_color not in AVAILABLE_RIM_COLORS:
        selected_color = AVAILABLE_RIM_COLORS[0]
        print(f"\tℹ️ Defaulting color to: {selected_color}")

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
    selected_crank_name = ""
    attempts = 0
    while not selected_crank_name:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_crank_name = crank_names[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_crank_name}"
            )
            break
        try:
            print("\n\tAvailable Crank Models:")
            for name in crank_names:
                info = CRANK_OPTIONS.get(name, {})
                interface = info.get("interface", "Standard")
                print(f"\t  [{crank_names.index(name) + 1}] {name} ({interface})")

            choice = int(input("\n\tSelect Crank Model (Enter number): ").strip())
            if choice < 1 or choice > len(crank_names):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_crank_name = crank_names[choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_crank_name = crank_names[0]
            break
        except Exception:
            logging.exception("Unexpected error during crank model selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    crank_info = CRANK_OPTIONS.get(selected_crank_name, {})
    interface = crank_info.get("interface", "Standard")
    available_lengths = crank_info.get("lengths", ["125mm"])
    colors = crank_info.get("available_colors", ["Black"])

    selected_length = ""
    attempts = 0
    while not selected_length:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_length = available_lengths[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_length}"
            )
            break
        try:
            print(f"\n\tAvailable Lengths:")
            for length in available_lengths:
                print(f"\t  [{available_lengths.index(length) + 1}] {length}")

            len_choice = int(input("\n\tSelect Length (Enter number): ").strip())
            if len_choice < 1 or len_choice > len(available_lengths):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_length = available_lengths[len_choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_length = available_lengths[0]
            break
        except Exception:
            logging.exception("Unexpected error during crank length selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    print(f"\n\tAvailable Colors: {', '.join(colors)}")
    color_choice = input("\tSelect Crank Color: ").strip().title()
    if color_choice not in colors:
        color_choice = colors[0]
        print(f"\tℹ️ Defaulting color to: {color_choice}")

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
    selected_brand = ""
    attempts = 0
    while not selected_brand:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_brand = pedal_brands[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_brand}"
            )
            break
        try:
            print("\n\tAvailable Pedal Makes:")
            for brand in pedal_brands:
                info = PEDAL_OPTIONS.get(brand, {})
                material = info.get("material", "Plastic platform")
                pins = info.get("pins", "Molded studs")
                print(
                    f"\t  [{pedal_brands.index(brand) + 1}] {brand} — {material} ({pins})"
                )

            choice = int(input("\n\tSelect Pedal Make (Enter number): ").strip())
            if choice < 1 or choice > len(pedal_brands):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_brand = pedal_brands[choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_brand = pedal_brands[0]
            break
        except Exception:
            logging.exception("Unexpected error during pedal selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    pedal_info = PEDAL_OPTIONS.get(selected_brand, {})
    material = pedal_info.get("material", "Plastic platform")
    pins = pedal_info.get("pins", "Molded studs")
    colors = pedal_info.get("available_colors", ["Black"])

    print(f"\n\tAvailable Colors: {', '.join(colors)}")
    selected_color = input("\tChoose Pedal Color: ").strip().title()
    if selected_color not in colors:
        selected_color = colors[0]
        print(f"\tℹ️ Defaulting color to: {selected_color}")

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
    selected_brake_name = ""
    attempts = 0
    while not selected_brake_name:
        attempts += 1
        if attempts > MAX_SELECTION_ATTEMPTS:
            selected_brake_name = brake_models[0]
            print(
                f"\n\tMaximum attempts reached. "
                f"Defaulting to: {selected_brake_name}"
            )
            break
        try:
            print("\n\tAvailable Brake Systems:")
            for model_name in brake_models:
                info = BRAKE_OPTIONS.get(model_name, {})
                mfr = info.get("manufacturer", "Generic")
                b_type = info.get("type", "Standard Disc")
                print(
                    f"\t  [{brake_models.index(model_name) + 1}] {model_name} — {mfr} ({b_type})"
                )

            choice = int(input("\n\tSelect Brake Model (Enter number): ").strip())
            if choice < 1 or choice > len(brake_models):
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_brake_name = brake_models[choice - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            selected_brake_name = brake_models[0]
            break
        except Exception:
            logging.exception("Unexpected error during brake model selection.")
            print(
                "\n\tUnexpected error. This operation cannot continue; "
                "see the error log for details."
            )
            raise

    brake_spec = BRAKE_OPTIONS.get(selected_brake_name, {})
    brake_type = brake_spec.get("type", "Hydraulic Disc")
    supported_rotors = brake_spec.get("supported_rotors_mm", [180])
    default_rotor = brake_spec.get("default_rotor_mm", 180)

    selected_rotor = "N/A"
    if supported_rotors:
        rotor_chosen = False
        attempts = 0
        while not rotor_chosen:
            attempts += 1
            if attempts > MAX_SELECTION_ATTEMPTS:
                selected_rotor = default_rotor
                print(
                    f"\n\tMaximum attempts reached. "
                    f"Defaulting rotor size to: {selected_rotor}mm"
                )
                break
            try:
                print(f"\n\tAvailable Rotor Sizes:")
                for size in supported_rotors:
                    print(f"\t  [{supported_rotors.index(size) + 1}] {size}mm Rotor")

                rotor_choice = int(
                    input("\n\tSelect Rotor Size (Enter number): ").strip()
                )
                if rotor_choice < 1 or rotor_choice > len(supported_rotors):
                    print("\n\tINVALID SELECTION - Please try again.")
                else:
                    selected_rotor = supported_rotors[rotor_choice - 1]
                    rotor_chosen = True
            except ValueError:
                print("\n\tINVALID SELECTION - Please try again.")
            except EOFError:
                print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
                selected_rotor = default_rotor
                rotor_chosen = True
                break
            except Exception:
                logging.exception("Unexpected error during rotor selection.")
                print(
                    "\n\tUnexpected error. This operation cannot continue; "
                    "see the error log for details."
                )
                raise

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

    full_name = input("\tEnter Full Name: ").strip()
    if full_name == "":
        full_name = "Valued Customer"

    email = input("\tEnter Email Address: ").strip()
    if email == "":
        email = "customer@example.com"

    address = input("\tEnter Billing Street Address: ").strip()
    if address == "":
        address = "123 Unicycle Way"

    city = input("\tEnter City: ").strip()
    if city == "":
        city = "Portland"

    state = input("\tEnter State (2 letters): ").strip().upper()
    if state == "":
        state = "OR"

    zip_code = input("\tEnter ZIP Code: ").strip()
    if zip_code == "":
        zip_code = "97201"

    payment_method = (
        input(
            "\tPayment Method [Credit Card / PayPal / Apple Pay] (Default: Credit Card): "
        )
        .strip()
        .title()
    )
    if payment_method == "":
        payment_method = "Credit Card"

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
        input("\tIs shipping address same as billing address? (y/n, Default: y): ")
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
        print("\tℹ️ Using billing address for shipping.")
    else:
        recipient_name = input("\tRecipient Full Name: ").strip()
        if recipient_name == "":
            recipient_name = "Valued Customer"

        street_address = input("\tShipping Street Address: ").strip()
        if street_address == "":
            street_address = "123 Unicycle Way"

        ship_city = input("\tCity: ").strip()
        if ship_city == "":
            ship_city = "Portland"

        ship_state = input("\tState: ").strip().upper()
        if ship_state == "":
            ship_state = "OR"

        ship_zip = input("\tZIP Code: ").strip()
        if ship_zip == "":
            ship_zip = "97201"

        ship_address = {
            "full_name": recipient_name,
            "address": street_address,
            "city": ship_city,
            "state": ship_state,
            "zip_code": ship_zip,
        }

    print("\n\tAvailable Shipping Options:")
    for key, method in SHIPPING_METHODS.items():
        print(
            f"\t  [{key}] {method['name']} — ${method['cost']:.2f} ({method['days']})"
        )

    choice = input("\n\tSelect Shipping Method (Enter number): ").strip()
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
    random_id = random.randint(10000, 99999)
    invoice_num = f"INV-{random_id}"
    invoice_header = f"Invoice ID: {invoice_num}"

    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'FLAMMEN RIDES UNICYCLES':^35}")
    print(f"\t{'ORDER INVOICE':^35}")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{invoice_header:^35}")

    base_price = 450.00

    # ℹ️ Resiliently extract sub-component data using .get()
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

    print("\n\t--- COMPONENT SUMMARY ---")
    print(
        f"\t  • Frame / Model:          {order_data.get('selected_model', 'Custom Unicycle')}"
    )
    wheel_display = order_data.get("wheel_size", '36"')
    print(f"\t  • Wheel Size:             {wheel_display}")
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
    print(f"\t  {dest.get('full_name', 'Valued Customer')}")
    print(
        f"\t  {dest.get('address', '123 Main St')}, {dest.get('city', 'Portland')}, {dest.get('state', 'OR')} {dest.get('zip_code', '97201')}"
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

    print("\n\tOrder Options:")
    print("\t  [1] Accept / Buy / Submit")
    print("\t  [2] Edit Customization")
    print("\t  [3] Cancel Order")

    choice = input("\n\tSelect choice (1-3): ").strip()

    if choice == "1":
        print(f"\n\t🎉 Order {invoice_num} has been successfully submitted!")
        return "SUBMITTED"
    elif choice == "2":
        print("\n\t🔄 Returning to customizer menu...")
        return "EDIT"
    else:
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
        frame_brand, selected_model, brakes_enabled = model_opts()

        # 📌 2. Tire & Wheel Assembly
        wheel_size = tire_opts()

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
