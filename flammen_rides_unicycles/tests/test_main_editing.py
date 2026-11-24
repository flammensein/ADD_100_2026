import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from flammen_rides_unicycles import main as configurator


class OrderEditingTests(unittest.TestCase):
    def test_frame_edit_refreshes_wheel_and_brake_dependents(self) -> None:
        order_data = {
            "frame_brand": "Old Brand",
            "selected_model": "Old Model",
            "wheel_size": '24"',
            "saddle": {"mount_style": "Pivotal"},
        }
        with (
            patch.object(configurator, "get_menu_choice", return_value="Frame"),
            patch.object(
                configurator,
                "model_opts",
                return_value=("New Brand", "New Model", '29"', False),
            ),
            patch.object(
                configurator, "tire_opts", return_value="New Tire"
            ) as tire,
            patch.object(
                configurator, "seat_post_opts", return_value={"post_model": "New Post"}
            ) as seat_post,
            patch.object(
                configurator, "rim_opts", return_value={"rim_model": "New Rim"}
            ) as rim,
            patch.object(
                configurator, "brake_opts", return_value={"brakes_installed": False}
            ) as brakes,
        ):
            updated_brakes_enabled = configurator._edit_order_section(
                order_data, True
            )

        self.assertEqual(order_data["wheel_size"], '29"')
        self.assertEqual(order_data["tire"], "New Tire")
        self.assertEqual(order_data["rim"], {"rim_model": "New Rim"})
        self.assertEqual(order_data["seat_post"], {"post_model": "New Post"})
        self.assertEqual(order_data["brakes"], {"brakes_installed": False})
        self.assertFalse(updated_brakes_enabled)
        tire.assert_called_once_with('29"')
        seat_post.assert_called_once_with(
            frame_brand="New Brand", saddle_mount_style="Pivotal"
        )
        rim.assert_called_once_with('29"')
        brakes.assert_called_once_with(brakes_enabled=False)

    def test_saddle_edit_refreshes_seatpost(self) -> None:
        order_data = {
            "frame_brand": "Current Brand",
            "saddle": {"mount_style": "Standard"},
        }
        with (
            patch.object(configurator, "get_menu_choice", return_value="Saddle"),
            patch.object(
                configurator,
                "saddle_opts",
                return_value={"mount_style": "Pivotal"},
            ),
            patch.object(
                configurator, "seat_post_opts", return_value={"post_model": "Pivotal"}
            ) as seat_post,
        ):
            configurator._edit_order_section(order_data, True)

        self.assertEqual(order_data["saddle"], {"mount_style": "Pivotal"})
        self.assertEqual(order_data["seat_post"], {"post_model": "Pivotal"})
        seat_post.assert_called_once_with(
            frame_brand="Current Brand", saddle_mount_style="Pivotal"
        )

    def test_billing_edit_reprompts_shipping(self) -> None:
        order_data = {"billing": {"full_name": "Old Customer"}}
        new_billing = {"full_name": "New Customer"}
        new_shipping = {"destination": {"full_name": "New Customer"}}
        with (
            patch.object(configurator, "get_menu_choice", return_value="Billing"),
            patch.object(configurator, "billing_info", return_value=new_billing),
            patch.object(
                configurator, "shipping_info", return_value=new_shipping
            ) as shipping,
        ):
            configurator._edit_order_section(order_data, True)

        self.assertEqual(order_data["billing"], new_billing)
        self.assertEqual(order_data["shipping"], new_shipping)
        shipping.assert_called_once_with(new_billing)

    def test_edit_returns_to_invoice_with_updated_order(self) -> None:
        order_data = {
            "wheel_size": '24"',
            "tire": "Old Tire",
            "billing": {},
            "shipping": {"shipping_cost": 10.0},
        }
        output = StringIO()
        with (
            patch.object(
                configurator,
                "generate_invoice_number",
                return_value="INV-EDIT",
            ),
            patch.object(
                configurator,
                "get_menu_choice",
                side_effect=["2", "Tire", "1"],
            ),
            patch.object(configurator, "tire_opts", return_value="New Tire"),
            patch.object(configurator, "format_invoice", return_value="Invoice"),
            patch.object(configurator, "create_order") as create_order,
            redirect_stdout(output),
        ):
            status = configurator.final_order(order_data, brakes_enabled=False)

        self.assertEqual(status, "SUBMITTED")
        self.assertEqual(order_data["tire"], "New Tire")
        saved_order = create_order.call_args.args[0]
        self.assertEqual(saved_order["tire"], "New Tire")
        self.assertEqual(saved_order["financials"]["shipping_cost"], 10.0)
        self.assertIn("successfully submitted", output.getvalue())


if __name__ == "__main__":
    unittest.main()
