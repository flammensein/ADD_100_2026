import json
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from flammen_rides_unicycles import order_storage
from flammen_rides_unicycles import main as configurator
from flammen_rides_unicycles.main import format_invoice


class OrderStorageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.orders_file = Path(self.temp_dir.name) / "orders.json"
        self.file_patch = patch.object(order_storage, "ORDERS_FILE", self.orders_file)
        self.file_patch.start()
        self.addCleanup(self.file_patch.stop)
        self.addCleanup(self.temp_dir.cleanup)

    def test_create_read_update_and_delete_orders(self) -> None:
        first = order_storage.create_order(
            {"invoice_num": "INV-ONE", "selected_model": "KH24"}
        )
        order_storage.create_order(
            {"invoice_num": "INV-TWO", "selected_model": "Oracle 29"}
        )

        updated = order_storage.update_order(
            first["invoice_num"], {"selected_model": "KH29"}
        )
        self.assertEqual(updated["selected_model"], "KH29")
        self.assertEqual(len(order_storage.read_orders()), 2)

        deleted = order_storage.delete_order("INV-ONE")
        self.assertEqual(deleted["invoice_num"], "INV-ONE")
        self.assertEqual(
            order_storage.read_orders(),
            [{"invoice_num": "INV-TWO", "selected_model": "Oracle 29"}],
        )

        with self.orders_file.open(encoding="utf-8") as file:
            self.assertEqual(json.load(file), order_storage.read_orders())

    def test_duplicate_invoice_is_rejected_without_overwriting_orders(self) -> None:
        order_storage.create_order({"invoice_num": "INV-ONE", "note": "keep"})

        with self.assertRaises(ValueError):
            order_storage.create_order({"invoice_num": "INV-ONE", "note": "replace"})

        self.assertEqual(
            order_storage.read_orders(),
            [{"invoice_num": "INV-ONE", "note": "keep"}],
        )

    def test_invoice_is_customer_readable(self) -> None:
        invoice = format_invoice(
            {
                "selected_model": "KH24 Mountain",
                "billing": {"full_name": "A. Customer"},
                "shipping": {
                    "destination": {
                        "full_name": "A. Customer",
                        "address": "1 Main St",
                        "city": "Example",
                        "state": "CA",
                        "zip_code": "90000",
                    },
                    "method_name": "Standard Ground",
                    "shipping_cost": 25.0,
                },
            },
            "INV-12345678",
            450.0,
            36.0,
            511.0,
        )

        self.assertIn("FLAMMEN RIDES UNICYCLES", invoice)
        self.assertIn("A. Customer", invoice)
        self.assertIn("INV-12345678", invoice)
        self.assertIn("TOTAL DUE:            $  511.00", invoice)
        self.assertLess(invoice.index("Invoice ID:"), invoice.index("FLAMMEN"))

    def test_submitted_invoice_is_displayed_and_persisted(self) -> None:
        order = {
            "selected_model": "KH24 Mountain",
            "billing": {"full_name": "A. Customer"},
            "shipping": {
                "destination": {
                    "full_name": "A. Customer",
                    "address": "1 Main St",
                    "city": "Example",
                    "state": "CA",
                    "zip_code": "90000",
                },
                "method_name": "Standard Ground",
                "shipping_cost": 25.0,
            },
        }
        output = StringIO()
        with (
            patch.object(
                configurator, "generate_invoice_number", return_value="INV-SUBMIT"
            ),
            patch.object(configurator, "get_menu_choice", return_value="1"),
            redirect_stdout(output),
        ):
            status = configurator.final_order(order)

        self.assertEqual(status, "SUBMITTED")
        self.assertIn("INV-SUBMIT", output.getvalue())
        self.assertIn("TOTAL DUE", output.getvalue())
        saved_orders = order_storage.read_orders()
        self.assertEqual(len(saved_orders), 1)
        self.assertEqual(saved_orders[0]["invoice_num"], "INV-SUBMIT")
        self.assertEqual(next(iter(saved_orders[0])), "invoice_num")
        self.assertEqual(saved_orders[0]["financials"]["total_cost"], 511.0)


if __name__ == "__main__":
    unittest.main()
