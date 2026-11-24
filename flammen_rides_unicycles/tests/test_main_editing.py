import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from flammen_rides_unicycles import main as configurator


class OrderEditingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.order_data = {
            "frame_brand": "Kris Holm Unicycles (KHU)",
            "selected_model": "KH24 Mountain",
            "wheel_size": '24"',
            "tire": 'Maxxis 24 x 2.4"',
            "saddle": {"mount_style": "Standard"},
            "seat_post": {"post_model": "KH Adjustable Standard Seatpost"},
            "rim": {"rim_model": "Qu-Ax DB-X Muni Rim"},
            "cranks": {"crank_model": "KH Spirit"},
            "brakes": {"brakes_installed": False},
            "billing": {"full_name": "Old Customer"},
            "shipping": {"shipping_cost": 10.0},
        }

    def test_frame_edit_changes_only_incompatible_components(self) -> None:
        order_data = self.order_data
        with (
            patch.object(
                configurator,
                "get_menu_choice",
                side_effect=["Frame", "Change Affected Sections"],
            ),
            patch.object(
                configurator,
                "model_opts",
                return_value=("Nimbus Unicycles", 'Oracle 29" Mountain', '29"', False),
            ),
            patch.object(
                configurator, "tire_opts", return_value='Maxxis 29 x 2.5"'
            ) as tire,
            patch.object(
                configurator,
                "seat_post_opts",
                return_value={"post_model": "Nimbus Standard Aluminum Seatpost"},
            ) as seat_post,
            patch.object(configurator, "rim_opts") as rim,
            patch.object(configurator, "brake_opts") as brakes,
        ):
            updated_brakes_enabled = configurator._edit_order_section(
                order_data, False
            )

        self.assertEqual(order_data["wheel_size"], '29"')
        self.assertEqual(order_data["tire"], 'Maxxis 29 x 2.5"')
        self.assertEqual(order_data["rim"], {"rim_model": "Qu-Ax DB-X Muni Rim"})
        self.assertEqual(
            order_data["seat_post"], {"post_model": "Nimbus Standard Aluminum Seatpost"}
        )
        self.assertEqual(order_data["brakes"], {"brakes_installed": False})
        self.assertEqual(order_data["cranks"], {"crank_model": "KH Spirit"})
        self.assertFalse(updated_brakes_enabled)
        tire.assert_called_once_with('29"')
        seat_post.assert_called_once_with(
            frame_seatpost_diameter_mm=25.4, saddle_mount_style="Standard"
        )
        rim.assert_not_called()
        brakes.assert_not_called()

    def test_saddle_edit_changes_incompatible_seatpost_only_with_consent(self) -> None:
        order_data = self.order_data
        with (
            patch.object(
                configurator,
                "get_menu_choice",
                side_effect=["Saddle", "Change Affected Sections"],
            ),
            patch.object(
                configurator,
                "saddle_opts",
                return_value={"mount_style": "Pivotal"},
            ),
            patch.object(
                configurator,
                "seat_post_opts",
                return_value={"post_model": "KH Forged Fixed Pivotal Seatpost"},
            ) as seat_post,
        ):
            configurator._edit_order_section(order_data, False)

        self.assertEqual(order_data["saddle"], {"mount_style": "Pivotal"})
        self.assertEqual(
            order_data["seat_post"], {"post_model": "KH Forged Fixed Pivotal Seatpost"}
        )
        seat_post.assert_called_once_with(
            frame_seatpost_diameter_mm=27.2, saddle_mount_style="Pivotal"
        )

    def test_compatible_saddle_edit_keeps_seatpost(self) -> None:
        with (
            patch.object(configurator, "get_menu_choice", return_value="Saddle") as menu,
            patch.object(
                configurator, "saddle_opts", return_value={"mount_style": "Standard"}
            ),
            patch.object(configurator, "seat_post_opts") as seat_post,
        ):
            configurator._edit_order_section(self.order_data, False)

        menu.assert_called_once()
        seat_post.assert_not_called()
        self.assertEqual(
            self.order_data["seat_post"]["post_model"], "KH Adjustable Standard Seatpost"
        )

    def test_billing_edit_reprompts_shipping(self) -> None:
        order_data = self.order_data
        new_billing = {"full_name": "New Customer"}
        new_shipping = {"destination": {"full_name": "New Customer"}}
        with (
            patch.object(configurator, "get_menu_choice", return_value="Billing"),
            patch.object(configurator, "billing_info", return_value=new_billing),
            patch.object(
                configurator, "shipping_info", return_value=new_shipping
            ) as shipping,
        ):
            configurator._edit_order_section(order_data, False)

        self.assertEqual(order_data["billing"], new_billing)
        self.assertEqual(order_data["shipping"], new_shipping)
        shipping.assert_called_once_with(new_billing)

    def test_seatpost_requires_matching_diameter_and_saddle_mount(self) -> None:
        with patch.object(
            configurator,
            "get_menu_choice",
            side_effect=["KH Forged Fixed Pivotal Seatpost", 350, "Double Bolt Clamp"],
        ) as menu:
            seatpost = configurator.seat_post_opts(
                27.2, "Pivotal"
            )

        self.assertEqual(
            menu.call_args_list[0].args[1], ["KH Forged Fixed Pivotal Seatpost"]
        )
        self.assertEqual(seatpost["post_model"], "KH Forged Fixed Pivotal Seatpost")
        with self.assertRaisesRegex(ValueError, "No seatposts are compatible"):
            configurator.seat_post_opts(25.4, "Pivotal")

    def test_rgb_frame_uses_31_6_pivotal_seatpost(self) -> None:
        diameter = configurator._frame_seatpost_diameter(
            "Qu-Ax Unicycles", 'RGB 29" Cross/Muni'
        )
        with (
            patch.object(
                configurator, "get_menu_choice", return_value="Kris Holm Fusion One"
            ) as saddle_menu,
            patch.object(configurator, "get_text_choice", side_effect=["Slim", "Black"]),
            patch.object(configurator, "get_validated_input", return_value="n"),
        ):
            saddle = configurator.saddle_opts(diameter)

        self.assertEqual(saddle_menu.call_args.args[1], ["Kris Holm Fusion One"])
        self.assertEqual(saddle["mount_style"], "Pivotal")
        with patch.object(
            configurator,
            "get_menu_choice",
            side_effect=["QU-AX Pivotal Seatpost", 500, "Double Bolt Clamp"],
        ) as menu:
            seatpost = configurator.seat_post_opts(diameter, "Pivotal")

        self.assertEqual(menu.call_args_list[0].args[1], ["QU-AX Pivotal Seatpost"])
        self.assertEqual(seatpost["diameter_mm"], 31.6)
        self.assertEqual(seatpost["length_mm"], 500)
        self.assertNotIn("Nimbus Air Saddle", configurator._compatible_saddles(diameter))
        self.assertIn("Kris Holm Fusion One", configurator._compatible_saddles(diameter))

    def test_post_matching_ignores_brand_and_rejects_wrong_diameter(self) -> None:
        compatible = configurator._compatible_seat_posts(25.4, "Standard")
        self.assertIn("Nimbus Standard Aluminum Seatpost", compatible)
        self.assertIn("Qu-Ax Gusseted Aluminum Seatpost", compatible)
        self.assertNotIn("KH Adjustable Standard Seatpost", compatible)
        self.assertNotIn("QU-AX Pivotal Seatpost", compatible)

    def test_missing_frame_diameter_reports_error(self) -> None:
        with patch.dict(
            configurator.UNICYCLE_BRANDS,
            {"Example": {"Model": {"wheel_size": '24"'}}},
            clear=True,
        ):
            with self.assertRaisesRegex(ValueError, "seatpost_diameter_mm"):
                configurator.model_opts()

    def test_unavailable_frame_is_omitted_from_menu(self) -> None:
        frames = {
            "Example": {
                "Available": {
                    "wheel_size": '24"',
                    "seatpost_diameter_mm": 25.4,
                    "disc_brakes_supported": False,
                },
                "Unavailable": {
                    "wheel_size": '24"',
                    "seatpost_diameter_mm": 30.0,
                    "disc_brakes_supported": False,
                },
            }
        }
        with (
            patch.dict(configurator.UNICYCLE_BRANDS, frames, clear=True),
            patch.object(
                configurator, "get_menu_choice", side_effect=["Example", "Available"]
            ) as menu,
        ):
            configurator.model_opts()

        self.assertEqual(menu.call_args_list[1].args[1], ["Available"])

    def test_same_diameter_frame_edit_retains_post_across_brands(self) -> None:
        order_data = self.order_data
        order_data.update(
            {
                "frame_brand": "Nimbus Unicycles",
                "selected_model": 'Oracle 24" Mountain',
                "seat_post": {"post_model": "Nimbus Standard Aluminum Seatpost"},
            }
        )
        with (
            patch.object(configurator, "get_menu_choice", return_value="Frame") as menu,
            patch.object(
                configurator,
                "model_opts",
                return_value=("Club Unicycles", 'Club 24"', '24"', False),
            ),
            patch.object(configurator, "seat_post_opts") as seat_post,
        ):
            configurator._edit_order_section(order_data, False)

        menu.assert_called_once()
        seat_post.assert_not_called()
        self.assertEqual(
            order_data["seat_post"]["post_model"], "Nimbus Standard Aluminum Seatpost"
        )

    def test_same_brand_frame_edit_checks_model_diameter(self) -> None:
        order_data = self.order_data
        order_data.update(
            {
                "frame_brand": "Qu-Ax Unicycles",
                "selected_model": 'Muni 24" Q-Axle',
                "seat_post": {"post_model": "Qu-Ax Gusseted Aluminum Seatpost"},
            }
        )
        with (
            patch.object(
                configurator,
                "get_menu_choice",
                side_effect=[
                    "Frame",
                    "Change Affected Sections",
                    "Change Affected Sections",
                ],
            ),
            patch.object(
                configurator,
                "model_opts",
                return_value=("Qu-Ax Unicycles", 'RGB 29" Cross/Muni', '29"', False),
            ),
            patch.object(configurator, "tire_opts", return_value='Maxxis 29 x 2.5"'),
            patch.object(
                configurator, "saddle_opts", return_value={"mount_style": "Pivotal"}
            ),
            patch.object(
                configurator,
                "seat_post_opts",
                return_value={"post_model": "QU-AX Pivotal Seatpost"},
            ) as seat_post,
        ):
            configurator._edit_order_section(order_data, False)

        self.assertEqual(order_data["seat_post"]["post_model"], "QU-AX Pivotal Seatpost")
        seat_post.assert_called_once_with(
            frame_seatpost_diameter_mm=31.6, saddle_mount_style="Pivotal"
        )

    def test_initial_saddle_choices_exclude_unavailable_frame_mounts(self) -> None:
        with (
            patch.object(
                configurator, "get_menu_choice", return_value="Nimbus Air Saddle"
            ) as menu,
            patch.object(configurator, "get_text_choice", return_value="Medium"),
        ):
            configurator.saddle_opts(frame_seatpost_diameter_mm=25.4)

        saddle_choices = menu.call_args.args[1]
        self.assertIn("Nimbus Air Saddle", saddle_choices)
        self.assertNotIn("Kris Holm Fusion One", saddle_choices)

    def test_incompatible_frame_edit_can_be_canceled(self) -> None:
        order_data = self.order_data
        order_data["saddle"] = {"mount_style": "Pivotal"}
        order_data["seat_post"] = {"post_model": "KH Forged Fixed Pivotal Seatpost"}
        original_order = dict(order_data)
        with (
            patch.object(
                configurator, "get_menu_choice", side_effect=["Frame", "Cancel Edit"]
            ),
            patch.object(
                configurator,
                "model_opts",
                return_value=("Nimbus Unicycles", 'Oracle 29" Mountain', '29"', False),
            ),
        ):
            brakes_enabled = configurator._edit_order_section(order_data, False)

        self.assertEqual(order_data, original_order)
        self.assertFalse(brakes_enabled)

    def test_cancel_after_resolving_first_conflicts_restores_entire_order(self) -> None:
        order_data = self.order_data
        order_data["saddle"] = {"mount_style": "Pivotal"}
        order_data["seat_post"] = {"post_model": "KH Forged Fixed Pivotal Seatpost"}
        original_order = dict(order_data)
        with (
            patch.object(
                configurator,
                "get_menu_choice",
                side_effect=["Frame", "Change Affected Sections", "Cancel Edit"],
            ),
            patch.object(
                configurator,
                "model_opts",
                return_value=("Nimbus Unicycles", 'Oracle 29" Mountain', '29"', False),
            ),
            patch.object(
                configurator, "tire_opts", return_value='Maxxis 29 x 2.5"'
            ),
            patch.object(
                configurator, "saddle_opts", return_value={"mount_style": "Standard"}
            ),
        ):
            configurator._edit_order_section(order_data, False)

        self.assertEqual(order_data, original_order)

    def test_frame_edit_can_resolve_saddle_then_seatpost(self) -> None:
        order_data = self.order_data
        order_data["saddle"] = {"mount_style": "Pivotal"}
        order_data["seat_post"] = {"post_model": "KH Forged Fixed Pivotal Seatpost"}
        with (
            patch.object(
                configurator,
                "get_menu_choice",
                side_effect=[
                    "Frame",
                    "Change Affected Sections",
                    "Change Affected Sections",
                ],
            ),
            patch.object(
                configurator,
                "model_opts",
                return_value=("Nimbus Unicycles", 'Oracle 29" Mountain', '29"', False),
            ),
            patch.object(configurator, "tire_opts", return_value='Maxxis 29 x 2.5"'),
            patch.object(
                configurator, "saddle_opts", return_value={"mount_style": "Standard"}
            ),
            patch.object(
                configurator,
                "seat_post_opts",
                return_value={"post_model": "Nimbus Standard Aluminum Seatpost"},
            ),
        ):
            configurator._edit_order_section(order_data, False)

        self.assertEqual(order_data["frame_brand"], "Nimbus Unicycles")
        self.assertEqual(order_data["saddle"]["mount_style"], "Standard")
        self.assertEqual(
            order_data["seat_post"]["post_model"], "Nimbus Standard Aluminum Seatpost"
        )

    def test_frame_brake_change_requires_consent_and_disables_brakes(self) -> None:
        order_data = self.order_data
        order_data["brakes"] = {"brakes_installed": True, "brake_model": "Current"}
        output = StringIO()
        with (
            patch.object(
                configurator,
                "get_menu_choice",
                side_effect=["Frame", "Change Affected Sections"],
            ),
            patch.object(
                configurator,
                "model_opts",
                return_value=(
                    "Kris Holm Unicycles (KHU)", "KH24 Mountain", '24"', False
                ),
            ),
            patch.object(
                configurator, "brake_opts", return_value={"brakes_installed": False}
            ) as brakes,
            redirect_stdout(output),
        ):
            enabled = configurator._edit_order_section(order_data, True)

        self.assertFalse(enabled)
        self.assertFalse(order_data["brakes"]["brakes_installed"])
        self.assertIn("brakes were disabled", output.getvalue())
        brakes.assert_called_once_with(brakes_enabled=False)

    def test_edit_returns_to_invoice_with_updated_order(self) -> None:
        order_data = self.order_data
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
            patch.object(configurator, "tire_opts", return_value='Nimbus 24 x 3.0"'),
            patch.object(configurator, "format_invoice", return_value="Invoice"),
            patch.object(configurator, "create_order") as create_order,
            redirect_stdout(output),
        ):
            status = configurator.final_order(order_data, brakes_enabled=False)

        self.assertEqual(status, "SUBMITTED")
        self.assertEqual(order_data["tire"], 'Nimbus 24 x 3.0"')
        saved_order = create_order.call_args.args[0]
        self.assertEqual(saved_order["tire"], 'Nimbus 24 x 3.0"')
        self.assertEqual(saved_order["financials"]["shipping_cost"], 10.0)
        self.assertIn("successfully submitted", output.getvalue())

    def test_build_displays_accumulated_selections_before_each_section(self) -> None:
        def choose(label, value):
            def selection(*args, **kwargs):
                print(f"BEGIN {label}")
                return value

            return selection

        output = StringIO()
        with (
            patch.object(
                configurator,
                "model_opts",
                side_effect=choose(
                    "Frame",
                    ("Kris Holm Unicycles (KHU)", "KH24 Mountain", '24"', False),
                ),
            ),
            patch.object(
                configurator, "tire_opts", side_effect=choose("Tire", "Tire choice")
            ),
            patch.object(
                configurator,
                "saddle_opts",
                side_effect=choose(
                    "Saddle", {"saddle_name": "Saddle choice", "mount_style": "Standard"}
                ),
            ),
            patch.object(
                configurator,
                "seat_post_opts",
                side_effect=choose("Seatpost", {"post_model": "Post choice"}),
            ),
            patch.object(
                configurator,
                "rim_opts",
                side_effect=choose("Rim", {"rim_model": "Rim choice"}),
            ),
            patch.object(
                configurator,
                "crank_opts",
                side_effect=choose("Cranks", {"crank_model": "Crank choice"}),
            ),
            patch.object(
                configurator,
                "pedal_opts",
                side_effect=choose("Pedals", {"pedal_brand": "Pedal choice"}),
            ),
            patch.object(
                configurator,
                "brake_opts",
                side_effect=choose("Brakes", {"brakes_installed": False}),
            ),
            patch.object(
                configurator,
                "billing_info",
                side_effect=choose("Billing", {"full_name": "Customer"}),
            ),
            patch.object(
                configurator,
                "shipping_info",
                side_effect=choose("Shipping", {"destination": {"city": "Example"}}),
            ),
            patch.object(configurator, "final_order") as final_order,
            redirect_stdout(output),
        ):
            configurator.main()

        text = output.getvalue()
        sections = [
            ("Frame", "No selections yet."),
            ("Tire", "Selected Model: KH24 Mountain"),
            ("Saddle", "Tire: Tire choice"),
            ("Seatpost", "Saddle Name: Saddle choice"),
            ("Rim", "Post Model: Post choice"),
            ("Cranks", "Rim Model: Rim choice"),
            ("Pedals", "Crank Model: Crank choice"),
            ("Brakes", "Pedal Brand: Pedal choice"),
            ("Billing", "Brakes Installed: False"),
            ("Shipping", "Full Name: Customer"),
        ]
        start = 0
        for label, selection in sections:
            end = text.index(f"BEGIN {label}", start)
            self.assertIn("Configuration selected so far", text[start:end])
            self.assertIn(selection, text[start:end])
            start = end + len(f"BEGIN {label}")

        saved = final_order.call_args.args[0]
        self.assertEqual(saved["shipping"]["destination"]["city"], "Example")
        self.assertFalse(final_order.call_args.args[1])


if __name__ == "__main__":
    unittest.main()
