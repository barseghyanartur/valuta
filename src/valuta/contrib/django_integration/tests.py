from decimal import Decimal
from django.test import TestCase, override_settings

import valuta

from product.models import (
    Product,
    ProductProxyCastToInt,
    ProductProxyCastToFloat,
    ProductProxyCastToDecimal,
    ProductProxyLimitChoicesTo,
)

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("DjangoIntegrationTestCase",)


class DjangoIntegrationTestCase(TestCase):
    def test_limit_choices_to(self):
        with self.subTest("Field choices"):
            self.assertListEqual(
                ProductProxyLimitChoicesTo.currency.field.choices,
                [("AMD", "Armenian Dram"), ("EUR", "Euro")],
            )

    # @override_settings(VALUTA_FIELD_LIMIT_CHOICES_TO=(
    #         (valuta.AMD.uid, valuta.AMD.name),
    #         (valuta.EUR.uid, valuta.EUR.name),
    # ))
    # def test_limit_choices_to_from_django_settings(self):
    #     from product.models import Product as ProductLimitChoicesFromSettings
    #     with self.subTest("Field choices from django settings"):
    #         self.assertListEqual(
    #             ProductLimitChoicesFromSettings.currency.field.choices,
    #             [("AMD", "Armenian Dram"), ("EUR", "Euro")],
    #         )

    def test_no_cast(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": valuta.EUR.uid,
            }
        )
        price_in_currency_units = p.price_in_currency_units()
        self.assertEqual(price_in_currency_units, 100)

        price_with_tax_in_currency_units = p.price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax_in_currency_units, 120)

    def test_cast_to_int(self):
        p = ProductProxyCastToInt.objects.create(
            **{
                "name": "My test product",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": valuta.EUR.uid,
            }
        )
        price_in_currency_units = p.price_in_currency_units()
        self.assertEqual(price_in_currency_units, 100)
        self.assertTrue(isinstance(price_in_currency_units, int))

        price_with_tax_in_currency_units = p.price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax_in_currency_units, 120)
        self.assertTrue(isinstance(price_in_currency_units, int))

    def test_cast_to_float(self):
        p = ProductProxyCastToFloat.objects.create(
            **{
                "name": "My test product",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": valuta.EUR.uid,
            }
        )
        price_in_currency_units = p.price_in_currency_units()
        self.assertEqual(price_in_currency_units, 100.0)
        self.assertTrue(isinstance(price_in_currency_units, float))

        price_with_tax_in_currency_units = p.price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax_in_currency_units, 120.0)
        self.assertTrue(isinstance(price_in_currency_units, float))

    def test_cast_to_decimal(self):
        p = ProductProxyCastToDecimal.objects.create(
            **{
                "name": "My test product",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": valuta.EUR.uid,
            }
        )
        price_in_currency_units = p.price_in_currency_units()
        self.assertEqual(price_in_currency_units, Decimal("100.0"))
        self.assertTrue(isinstance(price_in_currency_units, Decimal))

        price_with_tax_in_currency_units = p.price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax_in_currency_units, Decimal("120.0"))
        self.assertTrue(isinstance(price_in_currency_units, Decimal))
