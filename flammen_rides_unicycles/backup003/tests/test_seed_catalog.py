import unittest
from decimal import Decimal

from flammen_rides_unicycles.seed_catalog import build_seed_plan


class SeedCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = build_seed_plan()
        cls.products = {
            product["product_name"]: product for product in cls.plan["products"]
        }

    def test_dual_hole_crank_lengths_keep_both_measurements(self):
        variant = next(
            variant
            for variant in self.products["KH Boundary"]["variants"]
            if variant["display_label"] == "117/137mm dual hole"
        )

        self.assertEqual(
            [(value, sequence) for _, sequence, value, _ in variant["measurements"]],
            [(Decimal("117"), 1), (Decimal("137"), 2)],
        )

    def test_tire_size_maps_to_nominal_wheel_size(self):
        product = self.products['Maxxis 27.5 x 3.0"']

        self.assertEqual(product["wheel_sizes"], ['27.5"'])
        self.assertEqual(product["specs"]["width_in"], Decimal("3.0"))

    def test_clamp_style_colors_follow_style_configuration(self):
        styles = {style["style_label"]: style for style in self.plan["clamp_styles"]}

        self.assertFalse(styles["Double Bolt Clamp"]["color_customizable"])
        self.assertEqual(styles["Double Bolt Clamp"]["colors"], [])
        self.assertTrue(styles["Quick Release Clamp"]["color_customizable"])
        self.assertTrue(styles["Quick Release Clamp"]["colors"])


if __name__ == "__main__":
    unittest.main()
