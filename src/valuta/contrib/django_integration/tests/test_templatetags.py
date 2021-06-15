from django.test import TestCase

import valuta

from product.simple_models import SimpleProduct

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TemplateTagsTestCase",)


class TemplateTagsTestCase(TestCase):
    def setUp(self):
        self.product = SimpleProduct(
            currency_code=valuta.EUR.uid,
            price=1_000,
            price_with_tax=1_200,
        )

    def test_filter_convert_to_currency_units(self):
        p = self.product

        price = p.filter_product_price_in_currency_units()
        self.assertEqual(price, "10.0")

        price_with_tax = p.filter_product_price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax, "12.0")

    def test_tag_convert_to_currency_units(self):
        p = self.product

        price = p.tag_product_price_in_currency_units()
        self.assertEqual(price, "10.0")

        price_with_tax = p.tag_product_price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax, "12.0")
