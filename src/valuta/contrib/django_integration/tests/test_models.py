from decimal import Decimal

from django import VERSION
from django.utils.translation import gettext_lazy as _
from django.test import TestCase, override_settings

import valuta
from valuta.constants import DISPLAY_FORMAT_NUMBER
from valuta.contrib.django_integration.models import CurrencyField
from valuta.utils import get_currency_choices

from product.models import (
    AbstractProduct,
    Product,
    ProductProxyCastToInt,
    ProductProxyCastToFloat,
    ProductProxyCastToDecimal,
    ProductProxyLimitChoicesTo,
    ProductProxyChoicesFuncNone,
)

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("DjangoIntegrationTestCase",)


class DjangoIntegrationTestCase(TestCase):

    # ***********************************************************
    # *************** Convert to currency units *****************
    # ***********************************************************

    def test_limit_choices_to(self):
        with self.subTest("Field choices"):

            if VERSION[:2] > (2, 2):
                field = ProductProxyLimitChoicesTo.currency.field
            else:
                for field in ProductProxyLimitChoicesTo._meta.fields:
                    if field.name == "currency":
                        break

            self.assertListEqual(
                field.choices,
                [("AMD", "Armenian Dram (AMD)"), ("EUR", "Euro (EUR)")],
            )

    @override_settings(
        VALUTA_FIELD_LIMIT_CHOICES_TO=(
            valuta.AMD.uid,
            valuta.EUR.uid,
        ),
    )
    def test_limit_choices_to_from_django_settings(self):
        class ProductValueFieldLimitChoicesSettings(AbstractProduct):
            """Product model."""

            currency = CurrencyField(
                _("Currency"),
                amount_fields=(
                    "price",
                    "price_with_tax",
                ),
                get_choices_func=get_currency_choices,
            )

            class Meta:
                managed = False
                app_label = "product"
                db_table = Product._meta.db_table
                verbose_name = _(
                    "Product proxy (VALUTA_FIELD_LIMIT_CHOICES_TO)"
                )
                verbose_name_plural = _(
                    "Product proxies (VALUTA_FIELD_LIMIT_CHOICES_TO)"
                )

        with self.subTest("Field choices from django settings"):

            if VERSION[:2] > (2, 2):
                field = ProductValueFieldLimitChoicesSettings.currency.field
            else:
                for (
                    field
                ) in ProductValueFieldLimitChoicesSettings._meta.fields:
                    if field.name == "currency":
                        break

            self.assertListEqual(
                field.choices,
                [("AMD", "Armenian Dram"), ("EUR", "Euro")],
            )

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
        self.assertIsInstance(price_in_currency_units, int)

        price_with_tax_in_currency_units = p.price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax_in_currency_units, 120)
        self.assertIsInstance(price_in_currency_units, int)

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
        self.assertIsInstance(price_in_currency_units, float)

        price_with_tax_in_currency_units = p.price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax_in_currency_units, 120.0)
        self.assertIsInstance(price_in_currency_units, float)

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
        self.assertIsInstance(price_in_currency_units, Decimal)

        price_with_tax_in_currency_units = p.price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax_in_currency_units, Decimal("120.0"))
        self.assertIsInstance(price_in_currency_units, Decimal)

    def test_empty_currency_value(self):
        p = Product.objects.create(
            **{
                "name": "My test product 2",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": "",
            }
        )
        price_in_currency_units = p.price_in_currency_units()
        self.assertIsNone(price_in_currency_units)

    def test_invalid_currency_value(self):
        p = Product.objects.create(
            **{
                "name": "My test product 2",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": "INVALID",
            }
        )
        price_in_currency_units = p.price_in_currency_units()
        self.assertIsNone(price_in_currency_units)

    def test_get_choices_func_is_none(self):
        p = ProductProxyChoicesFuncNone.objects.create(
            **{
                "name": "My test product 3",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": valuta.EUR.uid,
            }
        )
        price_in_currency_units = p.price_in_currency_units()
        self.assertEqual(price_in_currency_units, 100)

        price_with_tax_in_currency_units = p.price_with_tax_in_currency_units()
        self.assertEqual(price_with_tax_in_currency_units, 120)

    def test_get_currency_cls(self):
        p = ProductProxyChoicesFuncNone.objects.create(
            **{
                "name": "My test product 4",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": valuta.EUR.uid,
            }
        )
        currency_cls = p.get_currency_cls_for_currency()
        self.assertEqual(currency_cls, valuta.EUR)

    def test_get_currency_cls_empty_currency_value(self):
        p = ProductProxyChoicesFuncNone.objects.create(
            **{
                "name": "My test product 5",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": "",
            }
        )
        currency_cls = p.get_currency_cls_for_currency()
        self.assertIsNone(currency_cls)

    def test_get_currency_cls_invalid_currency_value(self):
        p = ProductProxyChoicesFuncNone.objects.create(
            **{
                "name": "My test product 6",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": "INVALID",
            }
        )
        currency_cls = p.get_currency_cls_for_currency()
        self.assertIsNone(currency_cls)

    def test_1(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.UGX.uid,
            }
        )
        self.assertEqual(p.price_in_currency_units(), 1_000)

    def test_5(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.MRU.uid,
            }
        )
        self.assertEqual(p.price_in_currency_units(), 200)

    def test_10(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.VND.uid,
            }
        )
        self.assertEqual(p.price_in_currency_units(), 100)

    def test_100(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.EUR.uid,
            }
        )
        self.assertEqual(p.price_in_currency_units(), 10)

    def test_1000(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.TND.uid,
            }
        )
        self.assertEqual(p.price_in_currency_units(), 1)

    # ***********************************************************
    # *************** Display in currency units *****************
    # ***********************************************************

    def test_display_1_format_number(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.UGX.uid,
            }
        )
        self.assertEqual(
            p.price_display_in_currency_units(format=DISPLAY_FORMAT_NUMBER),
            "1000",
        )

    def test_display_5_format_number(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.MRU.uid,
            }
        )
        self.assertEqual(
            p.price_display_in_currency_units(format=DISPLAY_FORMAT_NUMBER),
            "200.00",
        )

    def test_display_10_format_number(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.VND.uid,
            }
        )
        self.assertEqual(
            p.price_display_in_currency_units(format=DISPLAY_FORMAT_NUMBER),
            "100",
        )

    def test_display_100_format_number(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.EUR.uid,
            }
        )
        self.assertEqual(
            p.price_display_in_currency_units(format=DISPLAY_FORMAT_NUMBER),
            "10.00",
        )

    def test_display_1000_format_number(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.TND.uid,
            }
        )
        self.assertEqual(
            p.price_display_in_currency_units(format=DISPLAY_FORMAT_NUMBER),
            "1.000",
        )

    def test_display_jpy_format_number(self):
        p = Product.objects.create(
            **{
                "name": "My test product",
                "price": 1_000,
                "price_with_tax": 1_200,
                "currency": valuta.JPY.uid,
            }
        )
        self.assertEqual(
            p.price_display_in_currency_units(format=DISPLAY_FORMAT_NUMBER),
            "10",
        )

    def test_display_empty_currency_value(self):
        p = Product.objects.create(
            **{
                "name": "My test product 2",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": "",
            }
        )
        price_display_in_currency_units = p.price_display_in_currency_units()
        self.assertIsNone(price_display_in_currency_units)

    def test_display_invalid_currency_value(self):
        p = Product.objects.create(
            **{
                "name": "My test product 2",
                "price": 10000,
                "price_with_tax": 12000,
                "currency": "INVALID",
            }
        )
        price_display_in_currency_units = p.price_display_in_currency_units()
        self.assertIsNone(price_display_in_currency_units)
