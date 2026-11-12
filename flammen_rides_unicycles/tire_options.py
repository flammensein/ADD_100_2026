# -----------------------------------------------------------------------
# SYSTEM CONSTANTS
# -----------------------------------------------------------------------
# AI prompt used to generate schema data:
# Generate a dictionary mapping tire brands to available tire models and
# dimensions.

TIRE_OPTIONS = {
    "Maxxis": ['20 x 2.5"', '27.5 x 3.0"'],
    "Nimbus": ['36 x 2.25"', '29 x 3.0"'],
    "Qu-Ax": ['36 x 2.25"'],
}


def tire_opts():
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
