# -----------------------------------------------------------------------
# SYSTEM CONSTANTS
# -----------------------------------------------------------------------
# AI prompt used to generate schema data:
# Generate a nested dictionary mapping unicycle rims to their specifications.

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


def rim_opts(wheel_size='36"'):
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
