"""Export the unicycle inventory dictionaries to menu.json."""

import json
from pathlib import Path

if __package__:
    from .dictionaries import (
        CRANK_OPTIONS,
        PEDAL_OPTIONS,
        RIM_OPTIONS,
        SADDLE_OPTIONS,
        SEAT_POST_OPTIONS,
        TIRE_OPTIONS,
        UNICYCLE_BRANDS,
    )
else:
    from dictionaries import (
        CRANK_OPTIONS,
        PEDAL_OPTIONS,
        RIM_OPTIONS,
        SADDLE_OPTIONS,
        SEAT_POST_OPTIONS,
        TIRE_OPTIONS,
        UNICYCLE_BRANDS,
    )


def get_menu_options():
    """Return all inventory dictionaries with their original nesting."""
    return {
        "UNICYCLE_BRANDS": UNICYCLE_BRANDS,
        "TIRE_OPTIONS": TIRE_OPTIONS,
        "SADDLE_OPTIONS": SADDLE_OPTIONS,
        "SEAT_POST_OPTIONS": SEAT_POST_OPTIONS,
        "RIM_OPTIONS": RIM_OPTIONS,
        "PEDAL_OPTIONS": PEDAL_OPTIONS,
        "CRANK_OPTIONS": CRANK_OPTIONS,
    }


def save_to_file(menu):
    """Replace menu.json with the supplied inventory as readable JSON."""
    menu_file = Path(__file__).with_name("menu.json")
    with menu_file.open("w", encoding="utf-8") as file:
        json.dump(menu, file, indent=2)
        file.write("\n")


def main():
    save_to_file(get_menu_options())


if __name__ == "__main__":
    main()
