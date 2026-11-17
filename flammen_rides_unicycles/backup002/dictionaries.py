# -----------------------------------------------------------------------
# SYSTEM DATA SCHEMAS & DICTIONARIES
# AI prompt used to generate schema data:
# Populate structured dictionaries for unicycle component customization,
# including brands, tires, saddles, seatposts, rims, pedals, and cranks.
# -----------------------------------------------------------------------

# Maps to model_opts() - Unicycle brands, models, and wheel sizes
UNICYCLE_BRANDS = {
    "Nimbus Unicycles": {
        'Hatchet 27.5" Mountain': {"wheel_size": '27.5"'},
        'Oracle 36"': {"wheel_size": '36"'},
    },
    "Kris Holm Unicycles (KHU)": {
        "KH20 Trials": {"wheel_size": '20"'},
        "KH36 Road/Touring": {"wheel_size": '36"'},
    },
    "Club Unicycles": {
        'Club 20" Beginner': {"wheel_size": '20"'},
        'Club 24"': {"wheel_size": '24"'},
    },
}

# Maps to tire_opts() - Tire brands and size offerings
TIRE_OPTIONS = {
    "Maxxis": ['20 x 2.5"', '27.5 x 3.0"'],
    "Nimbus": ['36 x 2.25"', '29 x 3.0"'],
    "Qu-Ax": ['36 x 2.25"'],
}

# Maps to saddle_opts() - Available saddle models grouped by brand
SADDLE_OPTIONS = {
    "Kris Holm": ["Fusion One"],
    "Nimbus": ["Air Saddle"],
    "Impact": ["Naomi"],
    "Club": ["Logo"],
}

# Maps to seat_post_opts() - Post specifications and frame compatibility
SEAT_POST_OPTIONS = {
    "KH Forged Fixed Pivotal Seatpost": {
        "lengths_mm": None,
        "diameter_mm": 27.2,
        "fits_brands": ["Kris Holm Unicycles (KHU)"],
    },
    "Nimbus Standard Aluminum Seatpost": {
        "lengths_mm": None,
        "diameter_mm": 25.4,
        "fits_brands": ["Nimbus Unicycles", "Club Unicycles"],
    },
}

# Maps to rim_opts(wheel_size) - Rim specifications and tire fitment
RIM_OPTIONS = {
    "KH Trials Rim": {
        "diameter_inches": 19,
        "construction": "double-wall",
        "width_mm": 47.2,
        "compatible_tire_sizes": ['20 x 2.5"'],
    },
    "Nimbus Nightrider Rim": {
        "diameter_inches": 36,
        "construction": "double-wall",
        "width_mm": 42.0,
        "compatible_tire_sizes": ['36 x 2.25"'],
    },
    "Nimbus Dominator Rim": {
        "diameter_inches": 29,
        "construction": "double-wall",
        "width_mm": None,
        "compatible_tire_sizes": ['29 x 3.0"'],
    },
}

# Maps to pedal_opts() - Pedal makes, platform materials, and pin styles
PEDAL_OPTIONS = {
    "Wellgo": {
        "material": "Clear polycarbonate platform",
        "pins": "removable steel pins",
    },
    "Nimbus": {
        "material": "Plastic platform",
        "pins": "molded studs",
    },
    "Kris Holm": {
        "material": "Plastic platform",
        "pins": "molded studs",
    },
}

# Maps to crank_opts() - Crank models, interface splines, and length options
CRANK_OPTIONS = {
    "KH Boundary": {
        "interface": "Q-Axle micro spline",
        "lengths": ["117/137mm dual hole", "127/150mm dual hole"],
    },
    "Nimbus VCX": {
        "interface": "ISIS / Standard",
        "lengths": ["125mm", "150mm"],
    },
    "Club Steel": {
        "interface": "cotterless, square-tapered",
        "lengths": ["114mm", "125mm"],
    },
}


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
