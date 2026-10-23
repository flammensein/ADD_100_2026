"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Flammen Rides Unicycles v0.2
Developer: Brent T. Marnati
"""

import uuid
from datetime import datetime

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
}

# Maps to crank_opts() - Crank models, interface splines, and length options
CRANK_OPTIONS = {
    "KH Boundary": {
        "brand": "Kris Holm",
        "interface": "Q-Axle micro spline",
        "lengths": ["117/137mm dual hole", "127/150mm dual hole"],
        "available_colors": ["Black", "Silver"],
    },
    "Nimbus VCX": {
        "brand": "Nimbus",
        "interface": "ISIS / Standard",
        "lengths": ["125mm", "150mm"],
        "available_colors": ["Black", "Silver", "Red"],
    },
    "Club Steel": {
        "brand": "Club",
        "interface": "Cotterless, square-tapered",
        "lengths": ["114mm", "125mm"],
        "available_colors": ["Black"],
    },
}

TIRE_OPTIONS = {
    "Maxxis": ['20 x 2.5"', '27.5 x 3.0"'],
    "Nimbus": ['36 x 2.25"', '29 x 3.0"'],
    "Qu-Ax": ['36 x 2.25"'],
}

# Add "supports_brakes": True to a model's options when it supports brakes.
BRAKE_OPTIONS = {
    "Shimano Deore M6100": {
        "manufacturer": "Shimano",
        "type": "Hydraulic Disc",
        "supported_rotors_mm": [160, 180],
        "default_rotor_mm": 180,
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
    "1": {
        "name": "Standard Ground",
        "cost": 25.00,
        "days": "3-5 business days",
    },
    "2": {
        "name": "Express 2-Day",
        "cost": 55.00,
        "days": "2 business days",
    },
    "3": {
        "name": "Overnight Freight",
        "cost": 95.00,
        "days": "1 business day",
    },
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
            model_info = {"brand": brand, "model": model, **options}
            if options.get("supports_brakes", False):
                while True:
                    brake_choice = (
                        input("Would you like to install brakes? (y/n): ")
                        .strip()
                        .lower()
                    )
                    if brake_choice in {"y", "n"}:
                        model_info["brakes_enabled"] = brake_choice == "y"
                        break
                    print("Please enter 'y' or 'n'.")
            else:
                model_info["brakes_enabled"] = False
                print("This model does not support brakes.")
            return model_info

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

    cushion_color = (
        input("Enter Cushion Color (e.g., Black, Blue, Red): ").strip().title()
    )
    if not cushion_color:
        cushion_color = "Black"

    leather_color = "N/A"
    if saddle_data.get("handle_leather_option", False):
        enable_leather = input("Enable Custom Leather Handle? (y/n): ").strip().lower()
        if enable_leather == "y":
            leather_color = (
                input("Enter Leather Color (e.g., Brown, Black, Tan): ").strip().title()
            )
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
    """Configure a crank model, length, interface, and color."""
    print("\n==========================================")
    print(" CRANK ARM SELECTION")
    print("==========================================")

    crank_names = list(CRANK_OPTIONS)
    print("\nAvailable Crank Models:")
    for index, name in enumerate(crank_names, start=1):
        info = CRANK_OPTIONS.get(name, {})
        interface = info.get("interface", "Standard")
        print(f" [{index}] {name} ({interface})")

    choice = input("\nSelect Crank Model (Enter number): ").strip()
    try:
        selected_crank_name = crank_names[int(choice) - 1]
    except (ValueError, IndexError):
        selected_crank_name = crank_names[0]
        print(f"Defaulting to: {selected_crank_name}")

    crank_info = CRANK_OPTIONS.get(selected_crank_name, {})
    interface = crank_info.get("interface", "Standard")
    available_lengths = crank_info.get("lengths", ["125mm"])
    colors = crank_info.get("available_colors", ["Black"])

    print(f"\nAvailable Lengths for {selected_crank_name}:")
    for index, length in enumerate(available_lengths, start=1):
        print(f" [{index}] {length}")

    length_choice = input("\nSelect Length (Enter number): ").strip()
    try:
        selected_length = available_lengths[int(length_choice) - 1]
    except (ValueError, IndexError):
        selected_length = available_lengths[0]
        print(f"Defaulting to: {selected_length}")

    print(f"\nAvailable Colors: {', '.join(colors)}")
    color_choice = input("Select Crank Color: ").strip().title()
    if color_choice not in colors:
        color_choice = colors[0]
        print(f"Defaulting color to: {color_choice}")

    print("\nSelected Cranks Configured:")
    print(f" • Model: {selected_crank_name}")
    print(f" • Interface: {interface}")
    print(f" • Length: {selected_length}")
    print(f" • Color: {color_choice}")

    return {
        "crank_model": selected_crank_name,
        "interface": interface,
        "length": selected_length,
        "color": color_choice,
    }


def pedal_opts():
    """Configure pedal make, platform, pin type, and color."""
    print("\n==========================================")
    print(" PEDAL SELECTION")
    print("==========================================")

    pedal_brands = list(PEDAL_OPTIONS)
    print("\nAvailable Pedal Makes:")
    for index, brand in enumerate(pedal_brands, start=1):
        info = PEDAL_OPTIONS.get(brand, {})
        material = info.get("material", "Plastic platform")
        pins = info.get("pins", "Molded studs")
        print(f" [{index}] {brand} — {material} ({pins})")

    choice = input("\nSelect Pedal Make (Enter number): ").strip()
    try:
        selected_brand = pedal_brands[int(choice) - 1]
    except (ValueError, IndexError):
        selected_brand = pedal_brands[0]
        print(f"Defaulting to: {selected_brand}")

    pedal_info = PEDAL_OPTIONS.get(selected_brand, {})
    material = pedal_info.get("material", "Plastic platform")
    pins = pedal_info.get("pins", "Molded studs")
    colors = pedal_info.get("available_colors", ["Black"])

    print(f"\nAvailable Colors for {selected_brand}: {', '.join(colors)}")
    selected_color = input("Choose Pedal Color: ").strip().title()
    if selected_color not in colors:
        selected_color = colors[0]
        print(f"Defaulting color to: {selected_color}")

    print("\nSelected Pedals Configured:")
    print(f" • Make: {selected_brand}")
    print(f" • Platform: {material}")
    print(f" • Pin Type: {pins}")
    print(f" • Color: {selected_color}")

    return {
        "pedal_brand": selected_brand,
        "material": material,
        "pins": pins,
        "color": selected_color,
    }


def brake_opts(brakes_enabled=True):
    """Configure a supported brake system, or return a bypassed configuration."""
    print("\n==========================================")
    print(" BRAKE SYSTEM SELECTION")
    print("==========================================")

    if not brakes_enabled:
        print("Brakes are not enabled or are not supported by the selected model.")
        return {
            "brakes_installed": False,
            "brake_model": "None",
            "type": "N/A",
            "rotor_diameter_mm": "N/A",
        }

    brake_models = list(BRAKE_OPTIONS)
    print("\nAvailable Brake Systems:")
    for index, model_name in enumerate(brake_models, start=1):
        info = BRAKE_OPTIONS.get(model_name, {})
        manufacturer = info.get("manufacturer", "Generic")
        brake_type = info.get("type", "Standard Disc")
        print(f" [{index}] {model_name} — {manufacturer} ({brake_type})")

    choice = input("\nSelect Brake Model (Enter number): ").strip()
    try:
        selected_brake_name = brake_models[int(choice) - 1]
    except (ValueError, IndexError):
        selected_brake_name = brake_models[0]
        print(f"Defaulting to: {selected_brake_name}")

    brake_spec = BRAKE_OPTIONS.get(selected_brake_name, {})
    brake_type = brake_spec.get("type", "Hydraulic Disc")
    supported_rotors = brake_spec.get("supported_rotors_mm", [])
    default_rotor = brake_spec.get("default_rotor_mm")
    selected_rotor = "N/A"

    if supported_rotors:
        print(f"\nAvailable Rotor Diameters for {selected_brake_name}:")
        for index, size in enumerate(supported_rotors, start=1):
            print(f" [{index}] {size}mm Rotor")

        rotor_choice = input("\nSelect Rotor Size (Enter number): ").strip()
        try:
            selected_rotor = supported_rotors[int(rotor_choice) - 1]
        except (ValueError, IndexError):
            selected_rotor = (
                default_rotor
                if default_rotor in supported_rotors
                else supported_rotors[0]
            )
            print(f"Defaulting rotor size to: {selected_rotor}mm")
    else:
        print("\nNo rotor required for this brake style.")

    print("\nSelected Brake System Configured:")
    print(f" • Model: {selected_brake_name}")
    print(f" • Type: {brake_type}")
    if selected_rotor == "N/A":
        print(" • Rotor: N/A")
    else:
        print(f" • Rotor Diameter: {selected_rotor}mm")

    return {
        "brakes_installed": True,
        "brake_model": selected_brake_name,
        "type": brake_type,
        "rotor_diameter_mm": selected_rotor,
    }


def billing_info():
    """Collect billing details and return them as a dictionary."""
    print("\n==========================================")
    print(" BILLING INFORMATION")
    print("==========================================")

    full_name = input("Enter Full Name: ").strip() or "Brent Marnati"
    email = input("Enter Email Address: ").strip() or "brent@example.com"
    address = input("Enter Billing Street Address: ").strip() or "123 Unicycle Way"
    city = input("Enter City: ").strip() or "Portland"
    state = input("Enter State (2 letters): ").strip().upper() or "OR"
    zip_code = input("Enter ZIP Code: ").strip() or "97201"
    payment_method = (
        input(
            "Payment Method [Credit Card / PayPal / Apple Pay] "
            "(Default: Credit Card): "
        )
        .strip()
        .title()
        or "Credit Card"
    )

    print("\nBilling Information Saved.")
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
    """Collect the delivery address and shipping method."""
    print("\n==========================================")
    print(" SHIPPING INFORMATION & METHOD")
    print("==========================================")

    same_as_billing = (
        input("Is shipping address same as billing address? (y/n): ").strip().lower()
    )
    if same_as_billing == "y" and billing_dict:
        ship_address = {
            "full_name": billing_dict.get("full_name", "Valued Customer"),
            "address": billing_dict.get("address", "123 Main St"),
            "city": billing_dict.get("city", "Portland"),
            "state": billing_dict.get("state", "OR"),
            "zip_code": billing_dict.get("zip_code", "97201"),
        }
        print("Using billing address for shipping.")
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
        print(
            f" [{key}] {method['name']} — ${method['cost']:.2f} " f"({method['days']})"
        )

    choice = input("\nSelect Shipping Method (Enter number): ").strip()
    selected = SHIPPING_METHODS.get(choice, SHIPPING_METHODS["1"])
    if choice not in SHIPPING_METHODS:
        print("Invalid selection. Defaulting to Standard Ground.")

    print(
        f"\nShipping Method Selected: {selected['name']} " f"(${selected['cost']:.2f})"
    )
    return {
        "destination": ship_address,
        "method_name": selected["name"],
        "shipping_cost": selected["cost"],
        "delivery_estimate": selected["days"],
    }


def final_order(order_data):
    """Display an itemized receipt and collect the user's order decision."""
    timestamp = datetime.now().strftime("%Y%m%d")
    unique_suffix = str(uuid.uuid4())[:4].upper()
    invoice_num = f"INV-{timestamp}-{unique_suffix}"

    print("\n==========================================================")
    print(" FLAMMEN RIDES UNICYCLES - ORDER INVOICE")
    print(f" Invoice ID: {invoice_num}")
    print("==========================================================")

    base_price = 450.00
    saddle = order_data.get("saddle", {})
    seat_post = order_data.get("seat_post", {})
    rim = order_data.get("rim", {})
    cranks = order_data.get("cranks", {})
    pedals = order_data.get("pedals", {})
    brakes = order_data.get("brakes", {})
    shipping = order_data.get("shipping", {})
    shipping_cost = shipping.get("shipping_cost", 25.00)
    tax_rate = 0.08
    tax_amount = base_price * tax_rate
    total_cost = base_price + shipping_cost + tax_amount

    print("\n--- COMPONENT SUMMARY ---")
    print(f" • Frame / Model: {order_data.get('frame_brand', 'Custom Unicycle')}")
    print(f" • Wheel Size: {order_data.get('wheel_size', '36\"')}")
    print(
        f" • Rim: {rim.get('rim_model', 'N/A')} " f"({rim.get('rim_color', 'Black')})"
    )
    print(
        f" • Saddle: {saddle.get('saddle_name', 'N/A')} "
        f"[{saddle.get('width', 'Medium')}]"
    )
    print(
        f" • Seatpost & Clamp: {seat_post.get('post_model', 'N/A')} "
        f"({seat_post.get('clamp_style', 'Standard')})"
    )
    print(
        f" • Crank Arms: {cranks.get('crank_model', 'N/A')} "
        f"({cranks.get('length', '125mm')})"
    )
    print(
        f" • Pedals: {pedals.get('pedal_brand', 'N/A')} "
        f"({pedals.get('color', 'Black')})"
    )
    print(
        f" • Brakes: {brakes.get('brake_model', 'None')} "
        f"({brakes.get('type', 'N/A')})"
    )

    print("\n--- SHIPPING DESTINATION ---")
    destination = shipping.get("destination", {})
    print(f" {destination.get('full_name', 'Valued Customer')}")
    print(
        f" {destination.get('address', '123 Main St')}, "
        f"{destination.get('city', 'Portland')}, "
        f"{destination.get('state', 'OR')} "
        f"{destination.get('zip_code', '97201')}"
    )
    print(
        f" Method: {shipping.get('method_name', 'Standard Ground')} "
        f"(${shipping_cost:.2f})"
    )

    print("\n--- FINANCIAL BREAKDOWN ---")
    print(f" Subtotal:             ${base_price:>8.2f}")
    print(f" Estimated Tax (8%):   ${tax_amount:>8.2f}")
    print(f" Shipping & Handling:  ${shipping_cost:>8.2f}")
    print(" -----------------------------------")
    print(f" TOTAL DUE:            ${total_cost:>8.2f}")
    print("==========================================================")

    print("\nOrder Options:")
    print(" [1] Accept / Buy / Submit")
    print(" [2] Edit Customization")
    print(" [3] Cancel Order")
    choice = input("\nSelect choice (1-3): ").strip()

    if choice == "1":
        print(f"\nOrder {invoice_num} has been successfully submitted!")
        return "SUBMITTED"
    if choice == "2":
        print("\nReturning to customizer menu...")
        return "EDIT"

    print("\nOrder canceled.")
    return "CANCELED"


def main():
    model_info = model_opts()
    frame_brand = model_info["brand"]
    brakes_enabled = model_info["brakes_enabled"]
    wheel_size = tire_opts()  # 🔄 Returns e.g. "36""
    rim_info = rim_opts(wheel_size)
    saddle_info = saddle_opts()
    seat_post_info = seat_post_opts(
        frame_brand=frame_brand,
        saddle_mount_style=saddle_info.get("mount_style", "Standard"),
    )
    crank_info = crank_opts()
    pedal_info = pedal_opts()
    brake_info = brake_opts(brakes_enabled=brakes_enabled)
    billing = billing_info()
    shipping = shipping_info(billing)
    order_data = {
        "frame_brand": frame_brand,
        "wheel_size": wheel_size,
        "rim": rim_info,
        "saddle": saddle_info,
        "seat_post": seat_post_info,
        "cranks": crank_info,
        "pedals": pedal_info,
        "brakes": brake_info,
        "billing": billing,
        "shipping": shipping,
    }
    final_order(order_data)


if __name__ == "__main__":
    main()
