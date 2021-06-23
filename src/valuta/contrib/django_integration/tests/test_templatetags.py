from django.test import TestCase

import valuta

from product.simple_models import SimpleProduct

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TemplateTagsTestCase",)


class TemplateTagsTestCase(TestCase):
    """Template tags."""

    # ***********************************************************
    # *************** Convert to currency units *****************
    # ***********************************************************

    def test_filter_convert_to_currency_units(self):
        p = SimpleProduct(
            currency_code=valuta.EUR.uid,
            price=1_000,
            price_with_tax=1_200,
        )

        price = p.filter_product_price_in_currency_units()
        self.assertEqual(price, "10.0")

        price_with_tax = p.filter_product_price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax, "12.0")

    def test_tag_convert_to_currency_units(self):
        p = SimpleProduct(
            currency_code=valuta.EUR.uid,
            price=1_000,
            price_with_tax=1_200,
        )

        price = p.tag_product_price_in_currency_units()
        self.assertEqual(price, "10.0")

        price_with_tax = p.tag_product_price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax, "12.0")

    # ***********************************************************
    # *************** Display in currency units *****************
    # ***********************************************************

    def test_filter_display_in_currency_units(self):
        with self.subTest("EUR"):
            p = SimpleProduct(
                currency_code=valuta.EUR.uid,
                price=1_000,
                price_with_tax=1_200,
            )

            price = p.filter_product_price_display_in_currency_units()
            self.assertEqual(price, "10.00")

            price_with_tax = (
                p.filter_product_price_with_tax_display_in_currency_units()
            )
            self.assertEqual(price_with_tax, "12.00")

        with self.subTest("JPY"):
            p = SimpleProduct(
                currency_code=valuta.JPY.uid,
                price=1_000,
                price_with_tax=1_200,
            )

            price = p.filter_product_price_display_in_currency_units()
            self.assertEqual(price, "10")

            price_with_tax = (
                p.filter_product_price_with_tax_display_in_currency_units()
            )
            self.assertEqual(price_with_tax, "12")

        with self.subTest("TND"):
            p = SimpleProduct(
                currency_code=valuta.TND.uid,
                price=1_000,
                price_with_tax=1_200,
            )

            price = p.filter_product_price_display_in_currency_units()
            self.assertEqual(price, "1.000")

            price_with_tax = (
                p.filter_product_price_with_tax_display_in_currency_units()
            )
            self.assertEqual(price_with_tax, "1.200")

    def test_tag_display_in_currency_units(self):
        with self.subTest("EUR"):
            p = SimpleProduct(
                currency_code=valuta.EUR.uid,
                price=1_000,
                price_with_tax=1_200,
            )

            price = p.tag_product_price_display_in_currency_units()
            self.assertEqual(price, "10.00")

            price_with_tax = (
                p.tag_product_price_with_tax_display_in_currency_units()
            )
            self.assertEqual(price_with_tax, "12.00")

        with self.subTest("JPY"):
            p = SimpleProduct(
                currency_code=valuta.JPY.uid,
                price=1_000,
                price_with_tax=1_200,
            )

            price = p.tag_product_price_display_in_currency_units()
            self.assertEqual(price, "10")

            price_with_tax = (
                p.tag_product_price_with_tax_display_in_currency_units()
            )
            self.assertEqual(price_with_tax, "12")

        with self.subTest("TND"):
            p = SimpleProduct(
                currency_code=valuta.TND.uid,
                price=1_000,
                price_with_tax=1_200,
            )

            price = p.tag_product_price_display_in_currency_units()
            self.assertEqual(price, "1.000")

            price_with_tax = (
                p.tag_product_price_with_tax_display_in_currency_units()
            )
            self.assertEqual(price_with_tax, "1.200")
