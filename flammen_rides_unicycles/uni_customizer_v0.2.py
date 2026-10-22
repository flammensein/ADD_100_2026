"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Flammen Rides Unicycles v0.2
Developer: Brent T. Marnati
"""

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

# Maps to saddle_opts() - Saddle specifications grouped by model
SADDLE_OPTIONS = {
    "Kris Holm Fusion One": {
        "brand": "Kris Holm",
        "mount_style": "Pivotal",
        "cushion_widths": ["Slim", "Medium"],
        "handle_leather_option": True,
    },
    "Nimbus Air Saddle": {
        "brand": "Nimbus",
        "mount_style": "Standard",
        "cushion_widths": ["Medium", "Wide"],
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

# Maps to seat_post_opts() - Post specifications and frame compatibility
SEAT_POST_OPTIONS = {
    "KH Forged Fixed Pivotal Seatpost": {
        "brand": "Kris Holm",
        "type": "Pivotal",
        "diameter_mm": 27.2,
        "lengths_mm": [],
        "compatible_brands": ["Kris Holm Unicycles (KHU)"],
    },
    "Nimbus Standard Aluminum Seatpost": {
        "brand": "Nimbus",
        "type": "Standard",
        "diameter_mm": 25.4,
        "lengths_mm": [],
        "compatible_brands": ["Nimbus Unicycles", "Club Unicycles"],
    },
}

CLAMP_STYLES = {
    "Double Bolt Clamp": {"color_customizable": False},
    "Quick Release Clamp": {"color_customizable": True},
}

CLAMP_COLORS = ["Black", "Silver", "Red", "Blue", "Gold"]

RIM_OPTIONS = {
    "KH Trials Rim": {
        "diameter_inches": 19,
        "construction": "double-wall",
        "width_mm": 47.2,
        "compatible_wheel_sizes": ['20"', '19"'],
    },
    "Nimbus Nightrider Rim": {
        "diameter_inches": 36,
        "construction": "double-wall",
        "width_mm": 42.0,
        "compatible_wheel_sizes": ['36"'],
    },
    "Nimbus Dominator Rim": {
        "diameter_inches": 29,
        "construction": "double-wall",
        "width_mm": None,
        "compatible_wheel_sizes": ['29"'],
    },
}

AVAILABLE_RIM_COLORS = ["Black", "Silver", "Red", "Blue"]


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

TIRE_OPTIONS = {
    "Maxxis": ['20 x 2.5"', '27.5 x 3.0"'],
    "Nimbus": ['36 x 2.25"', '29 x 3.0"'],
    "Qu-Ax": ['36 x 2.25"'],
}


def model_opts():
    # Frame size choice
    # Brakes Y/N choice (calls break_opts(brake_opts(yes) to brake_opts)
    # Frame color_options()
    #   - consider if multiple "color_options" lists will be needed or all colorized features can be made to work with a single list.
    # Returns frame_size, frame_color, brakes_yn, rotor_diameter {if brakes_yn(yes)}
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


def tire_opts():
    # Tire Brand
    # Tire Size (passes rim_opts(wheel_size) to restrict rim_size options)
    """Prompt the user to select a tire brand and size."""

    print("\n==========================================")
    print(" TIRE SELECTION")
    print("==========================================")

    available_brands = list(TIRE_OPTIONS.keys())
    print("\nAvailable Tire Brands:")
    for index, brand in enumerate(available_brands, start=1):
        print(f" [{index}] {brand}")

    brand_choice = input("\nSelect a Tire Brand (Enter number): ").strip()
    try:
        brand_idx = int(brand_choice) - 1
        selected_brand = available_brands[brand_idx]
    except (ValueError, IndexError):
        selected_brand = available_brands
        print(f"Invalid selection. Defaulting to: {selected_brand}")

    available_sizes = TIRE_OPTIONS.get(selected_brand, [])
    if not available_sizes:
        print("Warning: No specific tire sizes found for this brand.")
        available_sizes = ['36 x 2.25"']

    print(f"\nAvailable Sizes for {selected_brand}:")
    for index, size in enumerate(available_sizes, start=1):
        print(f" [{index}] {size}")

    size_choice = input("\nSelect a Tire Size (Enter number): ").strip()
    try:
        size_idx = int(size_choice) - 1
        selected_tire_size = available_sizes[size_idx]
    except (ValueError, IndexError):
        selected_tire_size = available_sizes
        print(f"Invalid selection. Defaulting to: {selected_tire_size}")

    # Extract the nominal wheel size from the tire string (for example, 36").
    raw_diameter = selected_tire_size.split()
    wheel_size = f'{raw_diameter}"'
    print("\nSelected Tire Configured:")
    print(f" • Brand: {selected_brand}")
    print(f" • Size: {selected_tire_size}")
    print(f" • Extracted Wheel Size: {wheel_size}")

    # Return wheel_size for main() to assign: wheel_size = tire_opts()
    return wheel_size


def saddle_opts():
    """Handle saddle selection, cushion customization, and leather options."""
    print("\n==========================================")
    print(" SADDLE SELECTION")
    print("==========================================")

    saddle_names = list(SADDLE_OPTIONS)
    print("\nAvailable Saddles:")
    for index, name in enumerate(saddle_names, start=1):
        info = SADDLE_OPTIONS.get(name, {})
        mount_style = info.get("mount_style", "Standard")
        print(f" [{index}] {name} ({mount_style} Mount)")

    choice = input("\nSelect Saddle (Enter number): ").strip()
    try:
        selected_saddle_name = saddle_names[int(choice) - 1]
    except (ValueError, IndexError):
        selected_saddle_name = saddle_names[0]
        print(f"Defaulting to: {selected_saddle_name}")

    saddle_data = SADDLE_OPTIONS.get(selected_saddle_name, {})
    mount_style = saddle_data.get("mount_style", "Standard")
    widths = saddle_data.get("cushion_widths", ["Medium"])

    print(f"\nAvailable Cushion Widths: {', '.join(widths)}")
    width_choice = input("Select Width: ").strip().title()
    if width_choice not in widths:
        width_choice = widths[0]
        print(f"Defaulting to: {width_choice}")

    cushion_color = input(
        "Enter Cushion Color (e.g., Black, Blue, Red): "
    ).strip().title()
    if not cushion_color:
        cushion_color = "Black"

    leather_color = "N/A"
    if saddle_data.get("handle_leather_option", False):
        enable_leather = input(
            "Enable Custom Leather Handle? (y/n): "
        ).strip().lower()
        if enable_leather == "y":
            leather_color = input(
                "Enter Leather Color (e.g., Brown, Black, Tan): "
            ).strip().title()
            if not leather_color:
                leather_color = "Brown"

    print("\nSelected Saddle Configured:")
    print(f" • Model: {selected_saddle_name}")
    print(f" • Mount Style: {mount_style}")
    print(f" • Width: {width_choice}")
    print(f" • Cushion Color: {cushion_color}")
    print(f" • Leather Handle: {leather_color}")

    return {
        "saddle_name": selected_saddle_name,
        "mount_style": mount_style,
        "width": width_choice,
        "cushion_color": cushion_color,
        "leather_color": leather_color,
    }


def seat_post_opts(
    frame_brand="Nimbus Unicycles",
    saddle_mount_style="Standard",
):
    """Configure a compatible seatpost, length, clamp style, and color."""
    print("\n==========================================")
    print(" SEATPOST & CLAMP SELECTION")
    print(
        f" (Filtering for Frame: '{frame_brand}', "
        f"Saddle Mount: '{saddle_mount_style}')"
    )
    print("==========================================")

    compatible_posts = []
    for post_name, specs in SEAT_POST_OPTIONS.items():
        post_type = specs.get("type", "Standard")
        brands = specs.get("compatible_brands", [])
        if frame_brand in brands or post_type == saddle_mount_style:
            compatible_posts.append(post_name)

    if not compatible_posts:
        print("Notice: No exact match found. Showing all seatpost options.")
        compatible_posts = list(SEAT_POST_OPTIONS)

    print("\nCompatible Seatposts:")
    for index, name in enumerate(compatible_posts, start=1):
        info = SEAT_POST_OPTIONS.get(name, {})
        diameter = info.get("diameter_mm", 25.4)
        post_type = info.get("type", "Standard")
        print(f" [{index}] {name} ({diameter}mm diameter, {post_type} Mount)")

    choice = input("\nSelect Seatpost (Enter number): ").strip()
    try:
        selected_post_name = compatible_posts[int(choice) - 1]
    except (ValueError, IndexError):
        selected_post_name = compatible_posts[0]
        print(f"Defaulting to: {selected_post_name}")

    post_info = SEAT_POST_OPTIONS.get(selected_post_name, {})
    available_lengths = post_info.get("lengths_mm", [])
    selected_length = None
    if available_lengths:
        print(
            "\nAvailable Lengths: "
            + ", ".join(f"{length}mm" for length in available_lengths)
        )
        length_choice = input("Select Length (in mm): ").strip()
        try:
            selected_length = int(length_choice)
        except ValueError:
            selected_length = available_lengths[0]

        if selected_length not in available_lengths:
            selected_length = available_lengths[0]
            print(f"Invalid length. Defaulting to: {selected_length}mm")
    else:
        print("No lengths are configured for this seatpost.")

    clamp_names = list(CLAMP_STYLES)
    print("\nAvailable Clamp Styles:")
    for index, clamp_name in enumerate(clamp_names, start=1):
        print(f" [{index}] {clamp_name}")

    clamp_choice = input("\nSelect Clamp Style (Enter number): ").strip()
    try:
        selected_clamp = clamp_names[int(clamp_choice) - 1]
    except (ValueError, IndexError):
        selected_clamp = clamp_names[0]
        print(f"Defaulting to: {selected_clamp}")

    clamp_spec = CLAMP_STYLES.get(selected_clamp, {})
    clamp_color = "Standard Black"
    if clamp_spec.get("color_customizable", False):
        print(f"\nAvailable Clamp Colors: {', '.join(CLAMP_COLORS)}")
        color_choice = input("Select Clamp Color: ").strip().title()
        if color_choice in CLAMP_COLORS:
            clamp_color = color_choice
        else:
            clamp_color = CLAMP_COLORS[0]
            print(f"Defaulting clamp color to: {clamp_color}")

    diameter = post_info.get("diameter_mm")
    print("\nSelected Seatpost & Clamp Configured:")
    print(f" • Post Model: {selected_post_name}")
    print(f" • Diameter: {diameter}mm")
    print(f" • Length: {selected_length if selected_length is not None else 'N/A'}")
    print(f" • Clamp Style: {selected_clamp} ({clamp_color})")

    return {
        "post_model": selected_post_name,
        "diameter_mm": diameter,
        "length_mm": selected_length,
        "clamp_style": selected_clamp,
        "clamp_color": clamp_color,
    }


def rim_opts(wheel_size):
    # Rim Style Options
    # wheel_size sets rim_size
    # Rim Color
    """Configure rim style and color based on the selected wheel size."""

    print(f"\n==========================================")
    print(f" RIM SELECTION (Target Wheel Size: {wheel_size})")
    print(f"==========================================")

    # Filter matching rims, using an empty list when compatibility is missing.
    matching_rims = []
    for rim_name, specs in RIM_OPTIONS.items():
        compatible_sizes = specs.get("compatible_wheel_sizes", [])
        if wheel_size in compatible_sizes:
            matching_rims.append(rim_name)

    # If no rim matches, show all available rims.
    if not matching_rims:
        print(
            f"Notice: No specific rim found for {wheel_size}. "
            "Displaying all options."
        )
        matching_rims = list(RIM_OPTIONS.keys())

    print("\nAvailable Rim Models:")
    for index, rim_name in enumerate(matching_rims, start=1):
        rim_info = RIM_OPTIONS.get(rim_name, {})
        construction = rim_info.get("construction", "standard construction")
        width = rim_info.get("width_mm", "N/A")
        width_str = f"{width}mm" if width is not None else "Width Unspecified"
        print(f" [{index}] {rim_name} — {construction} ({width_str})")

    choice = input("\nEnter choice number (Press Enter for option #1): ").strip()
    try:
        choice_idx = int(choice) - 1
        selected_rim_name = matching_rims[choice_idx]
    except (ValueError, IndexError):
        # Default to the first available rim when the choice is invalid.
        selected_rim_name = matching_rims[0]
        print(f"Defaulting to: {selected_rim_name}")

    selected_specs = RIM_OPTIONS.get(selected_rim_name, {})
    final_width = selected_specs.get("width_mm", "Standard")
    final_construction = selected_specs.get("construction", "Single-wall")

    print(f"\nAvailable Colors: {', '.join(AVAILABLE_RIM_COLORS)}")
    selected_color = input("Choose a rim color: ").strip().title()
    if selected_color not in AVAILABLE_RIM_COLORS:
        selected_color = AVAILABLE_RIM_COLORS[0]
        print(f"Invalid or unselected color. Defaulting to: {selected_color}")

    print("\nSelected Rim Configured:")
    print(f" • Model: {selected_rim_name}")
    print(f" • Color: {selected_color}")
    print(f" • Build: {final_construction} ({final_width}mm)")

    return {
        "rim_model": selected_rim_name,
        "rim_color": selected_color,
        "width_mm": final_width,
        "construction": final_construction,
    }


def crank_opts():
    # Crank Model/Length
    # Crank Color
    pass


def pedal_opts():
    # Pedal Make/Model
    pass


def brake_opts():
    # Only available if model_opts() selection makes it so.
    # Brake Make/Model
    # Rotor Diameter
    pass


def billing_info():
    # Collect Billing information
    pass


def shipping_info():
    # Collect shipping destination
    # Calculate shipping cost options based on destination, and weight
    # Present user with shipping options and the cost of each to
    # ==> Collect shipping method choice
    # Collect
    pass


def final_order():
    # Builds onscreen presentation of order with generated unique Order ID (invoice_num)
    # Offers 'Accept/Buy/Submit', 'Edit', 'Cancel' options.
    # Proceeds accordingly
    pass


def main():
    model_info = model_opts()
    frame_brand = model_info["brand"]
    wheel_size = tire_opts()  # 🔄 Returns e.g. "36""
    saddle_info = saddle_opts()
    seat_post_opts(
        frame_brand=frame_brand,
        saddle_mount_style=saddle_info.get("mount_style", "Standard"),
    )
    rim_opts(wheel_size)  # ⚙️ Pass wheel_size to restrict rim options!
    crank_opts()
    pedal_opts()
    brake_opts()
    billing_info()
    shipping_info()
    final_order()


main()
