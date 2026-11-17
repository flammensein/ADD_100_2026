"""Persistent JSON storage for submitted unicycle orders."""

import json
import os
import tempfile
from pathlib import Path
from uuid import uuid4

ORDERS_FILE: Path = Path(__file__).with_name("orders.json")
# ℹ️ Order records contain mixed JSON values, so their annotations stay at dict/list level.


def read_orders() -> list:
    """Read all saved orders, returning an empty list before the first order."""
    if not ORDERS_FILE.exists():
        return []

    # 📁 JSON parsing is O(n) in the size of the order-history file.
    with ORDERS_FILE.open(encoding="utf-8") as file:
        orders = json.load(file)

    if not isinstance(orders, list) or any(
        not isinstance(order, dict)
        or not isinstance(order.get("invoice_num"), str)
        for order in orders
    ):
        raise ValueError(f"{ORDERS_FILE.name} must contain a list of orders.")
    return orders


def generate_invoice_number() -> str:
    """Generate an invoice identifier not already present in the order file."""
    # 🧠 Build the existing-ID set in O(n); membership checks are O(1) on average.
    existing_numbers = {order["invoice_num"] for order in read_orders()}
    while True:
        invoice_num = f"INV-{uuid4().hex[:8].upper()}"
        if invoice_num not in existing_numbers:
            return invoice_num


def _write_orders(orders: list) -> None:
    """Atomically replace the order file so interrupted writes don't truncate it."""
    temporary_path = None
    try:
        # 💾 A same-directory temporary file keeps os.replace on one filesystem.
        # 🧠 JSON serialization and replacement are O(n) in the saved history.
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=ORDERS_FILE.parent,
            prefix=f".{ORDERS_FILE.name}.",
            suffix=".tmp",
            delete=False,
        ) as file:
            temporary_path = Path(file.name)
            json.dump(orders, file, indent=2)
            file.write("\n")
        os.replace(temporary_path, ORDERS_FILE)
        temporary_path = None
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def create_order(order: dict) -> dict:
    """Persist a new order without replacing previously submitted orders."""
    invoice_num = order.get("invoice_num")
    if not isinstance(invoice_num, str) or not invoice_num:
        raise ValueError("An order must include a non-empty invoice_num.")

    orders = read_orders()
    if any(saved["invoice_num"] == invoice_num for saved in orders):
        raise ValueError(f"Order {invoice_num} already exists.")

    # 💾 Reading, checking, and rewriting the history make order creation O(n).
    saved_order = {"invoice_num": invoice_num}
    saved_order.update(
        {key: value for key, value in order.items() if key != "invoice_num"}
    )
    orders.append(saved_order)
    _write_orders(orders)
    return saved_order


def update_order(invoice_num: str, updates: dict) -> dict:
    """Update an existing order while preserving its invoice identifier."""
    if "invoice_num" in updates:
        raise ValueError("An order's invoice_num cannot be changed.")

    orders = read_orders()
    # 🧠 Finding the order and rewriting JSON are both O(n) in saved order count.
    for index, order in enumerate(orders):
        if order["invoice_num"] == invoice_num:
            updated_order = dict(order)
            updated_order.update(updates)
            orders[index] = updated_order
            _write_orders(orders)
            return updated_order

    raise KeyError(f"Order {invoice_num} was not found.")


def delete_order(invoice_num: str) -> dict:
    """Remove and return a saved order."""
    orders = read_orders()
    # 🧠 Locate and remove one record in O(n), then rewrite the remaining history.
    for index, order in enumerate(orders):
        if order["invoice_num"] == invoice_num:
            deleted_order = orders.pop(index)
            _write_orders(orders)
            return deleted_order

    raise KeyError(f"Order {invoice_num} was not found.")
