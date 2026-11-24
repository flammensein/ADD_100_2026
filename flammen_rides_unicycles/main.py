"""
-----------------------------------------------------------------------
ASSIGNMENT 13B: Python Portion of Final
Project: Flammen Rides Unicycles v1.0.0
-----------------------------------------------------------------------
"""

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


def model_opts() -> tuple:
    """
    Prompt user for unicycle brand, model, and brake setup preference.
    Return selected frame brand, model, wheel size, and brake preference.
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
    brakes_yn = _select_brakes_enabled(
        model_spec.get("disc_brakes_supported", True)
    )
    wheel_size = model_spec["wheel_size"]
    # ✅ Return: (selected_brand, selected_model, wheel_size, brakes_yn) (tuple)
    return selected_brand, selected_model, wheel_size, brakes_yn


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
    compatible_sizes_by_brand = {
        brand: [size for size in sizes if f'{size.split()[0]}"' == frame_wheel_size]
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
    # ✅ Return: selected_tire (str)
    return selected_tire


def saddle_opts() -> dict:
    """
    Configure saddle model, cushion width, cushion color, and optional handle leather.
    Return saddle details dictionary including mount_style.
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

    # ✅ Return: saddle configuration (dict)
    return {
        "saddle_name": selected_saddle_name,
        "mount_style": mount_style,
        "width": width_choice,
        "cushion_color": cushion_color,
        "leather_color": leather_color,
    }


def seat_post_opts(
    frame_brand: str = "Nimbus Unicycles", saddle_mount_style: str = "Standard"
) -> dict:
    """
    Filter seatposts by frame brand compatibility and saddle mount type (Pivotal vs Standard).
    Configure post length, clamp style, and optional clamp color customization.
    """
    print(f"\n\n")
    print(f"\t{'=' * 35:^35}")
    print(f"\t{'SEATPOST & CLAMP SELECTION':^35}")
    print(f"\t{'=' * 35:^35}")

    # 🧠 Scan each catalog post once (O(n)); accept brand-compatible or matching mounts.
    # ℹ️ Future changes should keep the mount and brand checks aligned with catalog specs.
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

    # ✅ Return: seatpost and clamp configuration (dict)
    return {
        "post_model": selected_post_name,
        "diameter_mm": post_info.get("diameter_mm"),
        "length_mm": selected_length,
        "clamp_style": selected_clamp,
        "clamp_color": clamp_color,
    }


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


def _edit_order_section(order_data: dict, brakes_enabled: bool) -> bool:
    """Edit one order section and refresh any components that depend on it."""
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

    if section == "Frame":
        frame_brand, selected_model, wheel_size, brakes_enabled = model_opts()
        order_data.update(
            {
                "frame_brand": frame_brand,
                "selected_model": selected_model,
                "wheel_size": wheel_size,
            }
        )
        order_data["tire"] = tire_opts(wheel_size)
        order_data["seat_post"] = seat_post_opts(
            frame_brand=frame_brand,
            saddle_mount_style=order_data["saddle"].get(
                "mount_style", "Standard"
            ),
        )
        order_data["rim"] = rim_opts(wheel_size)
        order_data["brakes"] = brake_opts(brakes_enabled=brakes_enabled)
    elif section == "Tire":
        order_data["tire"] = tire_opts(order_data["wheel_size"])
    elif section == "Saddle":
        order_data["saddle"] = saddle_opts()
        order_data["seat_post"] = seat_post_opts(
            frame_brand=order_data["frame_brand"],
            saddle_mount_style=order_data["saddle"].get(
                "mount_style", "Standard"
            ),
        )
    elif section == "Seatpost":
        order_data["seat_post"] = seat_post_opts(
            frame_brand=order_data["frame_brand"],
            saddle_mount_style=order_data["saddle"].get(
                "mount_style", "Standard"
            ),
        )
    elif section == "Rim":
        order_data["rim"] = rim_opts(order_data["wheel_size"])
    elif section == "Cranks":
        order_data["cranks"] = crank_opts()
    elif section == "Pedals":
        order_data["pedals"] = pedal_opts()
    elif section == "Brakes":
        model_spec = UNICYCLE_BRANDS[order_data["frame_brand"]][
            order_data["selected_model"]
        ]
        brakes_enabled = _select_brakes_enabled(
            model_spec.get("disc_brakes_supported", True)
        )
        order_data["brakes"] = brake_opts(brakes_enabled=brakes_enabled)
    elif section == "Billing":
        order_data["billing"] = billing_info()
        order_data["shipping"] = shipping_info(order_data["billing"])
    else:
        order_data["shipping"] = shipping_info(order_data["billing"])

    return brakes_enabled


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

        print(
            format_invoice(
                order_data, invoice_num, subtotal, tax_amount, total_cost
            )
        )

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
    # 🧠 STEP 1: Select frame & establish wheel_size and brake support
    frame_brand, selected_model, wheel_size, brakes_enabled = model_opts()

    # 🧠 STEP 2: Select tire filtered by frame wheel_size
    selected_tire = tire_opts(wheel_size)

    # 🧠 STEP 3: Configure saddle & pair seatpost with frame brand or saddle mount
    saddle_dict = saddle_opts()
    seat_post_dict = seat_post_opts(
        frame_brand=frame_brand,
        saddle_mount_style=saddle_dict.get("mount_style", "Standard"),
    )

    # 🧠 STEP 4: Select rim filtered by frame wheel_size
    rim_dict = rim_opts(wheel_size)

    # 🧠 STEP 5: Configure drivetrain (cranks and pedals)
    crank_dict = crank_opts()
    pedal_dict = pedal_opts()

    # 🧠 STEP 6: Configure brakes (bypassed if unsupported or declined)
    brake_dict = brake_opts(brakes_enabled=brakes_enabled)

    # 🧠 STEP 7: Collect billing & shipping (with billing address reuse option)
    billing_dict = billing_info()
    shipping_dict = shipping_info(billing_dict)

    # 🧠 STEP 8: Consolidate selections into a single order dictionary for checkout
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

    final_order(order_data, brakes_enabled)


# ▶️ Imports expose functions without starting checkout; direct execution starts the app.
if __name__ == "__main__":
    main()
