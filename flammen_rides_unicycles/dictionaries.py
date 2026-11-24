"""Load the product catalog from product_catalog.json."""

import json
from pathlib import Path
from typing import Any

_REQUIRED_CATALOG_KEYS = (
    "UNICYCLE_BRANDS",
    "TIRE_OPTIONS",
    "SADDLE_OPTIONS",
    "SEAT_POST_OPTIONS",
    "CLAMP_STYLES",
    "RIM_OPTIONS",
    "CRANK_OPTIONS",
    "PEDAL_OPTIONS",
    "BRAKE_OPTIONS",
    "AVAILABLE_RIM_COLORS",
    "SADDLE_CUSHION_COLORS",
    "SADDLE_LEATHER_COLORS",
    "CLAMP_COLORS",
)


def _load_catalog() -> dict[str, Any]:
    catalog_file = Path(__file__).with_name("product_catalog.json")
    with catalog_file.open(encoding="utf-8") as file:
        catalog = json.load(file)

    if not isinstance(catalog, dict):
        raise ValueError(f"{catalog_file.name} must contain a JSON object.")

    missing_keys = [key for key in _REQUIRED_CATALOG_KEYS if key not in catalog]
    if missing_keys:
        raise ValueError(
            f"{catalog_file.name} is missing catalog sections: "
            + ", ".join(missing_keys)
        )
    return catalog


try:
    _CATALOG = _load_catalog()
except (OSError, ValueError) as exc:
    raise RuntimeError(f"Could not load product_catalog.json: {exc}") from exc

UNICYCLE_BRANDS = _CATALOG["UNICYCLE_BRANDS"]
TIRE_OPTIONS = _CATALOG["TIRE_OPTIONS"]
SADDLE_OPTIONS = _CATALOG["SADDLE_OPTIONS"]
SEAT_POST_OPTIONS = _CATALOG["SEAT_POST_OPTIONS"]
CLAMP_STYLES = _CATALOG["CLAMP_STYLES"]
RIM_OPTIONS = _CATALOG["RIM_OPTIONS"]
CRANK_OPTIONS = _CATALOG["CRANK_OPTIONS"]
PEDAL_OPTIONS = _CATALOG["PEDAL_OPTIONS"]
BRAKE_OPTIONS = _CATALOG["BRAKE_OPTIONS"]
AVAILABLE_RIM_COLORS = _CATALOG["AVAILABLE_RIM_COLORS"]
SADDLE_CUSHION_COLORS = _CATALOG["SADDLE_CUSHION_COLORS"]
SADDLE_LEATHER_COLORS = _CATALOG["SADDLE_LEATHER_COLORS"]
CLAMP_COLORS = _CATALOG["CLAMP_COLORS"]
