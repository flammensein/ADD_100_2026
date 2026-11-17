# Product catalog data used by the unicycle customization flow.
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

TIRE_OPTIONS = {
    "Maxxis": ['20 x 2.5"', '24 x 2.4"', '27.5 x 3.0"', '29 x 2.5"'],
    "Nimbus": ['24 x 3.0"', '29 x 3.0"', '36 x 2.25"'],
    "Qu-Ax": ['24 x 3.0"', '27.5 x 2.6"', '36 x 2.25"'],
    "Schwalbe": ['24 x 2.6"', '27.5 x 2.8"', '29 x 2.6"'],
    "Duro": ['24 x 3.0"', '27.5 x 3.25"'],
}

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

CLAMP_STYLES = {
    "Double Bolt Clamp": {"color_customizable": False},
    "Quick Release Clamp": {"color_customizable": True},
    "Triple Bolt Muni Clamp": {"color_customizable": True},
}

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

AVAILABLE_RIM_COLORS = ["Black", "Silver", "Red", "Blue", "Green", "Gold"]
SADDLE_CUSHION_COLORS = ["Black", "Brown", "Red", "Blue", "Green"]
SADDLE_LEATHER_COLORS = ["Black", "Brown", "Red", "Blue"]
CLAMP_COLORS = ["Black", "Silver", "Red", "Blue", "Gold", "Green", "Orange"]


def model_opts():
    """Display the available unicycle models and return the user's selection."""
    models = [
        (brand, model, options)
        for brand, brand_models in UNICYCLE_BRANDS.items()
        for model, options in brand_models.items()
    ]

    print("Available unicycle models:")
    for index, (brand, model, options) in enumerate(models, start=1):
        print(f"{index}. {brand} - {model} ({options['wheel_size']} wheel)")

    while True:
        selection = input(f"Select a model (1-{len(models)}): ")
        try:
            index = int(selection)
        except ValueError:
            print("Please enter a number from the list.")
            continue

        if 1 <= index <= len(models):
            brand, model, options = models[index - 1]
            return {"brand": brand, "model": model, **options}

        print(f"Please enter a number from 1 to {len(models)}.")
