from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

import valuta
from valuta.utils import get_currency_choices, get_currency_choices_with_code
from valuta.contrib.django_integration.models import CurrencyField

from .helpers import get_currency_choices_with_sign

__all__ = (
    "AbstractProduct",
    "Product",
    "ProductProxyCastToInt",
    "ProductProxyCastToFloat",
    "ProductProxyCastToDecimal",
    "ProductProxyLimitChoicesTo",
    "ProductProxyChoicesFuncNone",
)


class AbstractProduct(models.Model):
    """Abstract product model."""

    name = models.CharField(_("Name"), max_length=255)
    price = models.IntegerField(_("Price"))
    price_with_tax = models.IntegerField(_("Price with tax"))

    class Meta:
        abstract = True
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Product(AbstractProduct):
    """Product model."""

    currency = CurrencyField(
        _("Currency"),
        amount_fields=(
            "price",
            "price_with_tax",
        ),
        get_choices_func=get_currency_choices_with_code,
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductProxyCastToInt(AbstractProduct):
    """A sort of a proxy model to Product.

    Casts amount in fractional units to int.
    """

    currency = CurrencyField(
        _("Currency"),
        amount_fields=(
            "price",
            "price_with_tax",
        ),
        cast_to=int,
    )

    class Meta:
        managed = False
        db_table = Product._meta.db_table
        verbose_name = _("Product proxy (cast_to=int)")
        verbose_name_plural = _("Product proxies (cast_to=int)")


class ProductProxyCastToFloat(AbstractProduct):
    """A sort of a proxy model to Product.

    Casts amount in fractional units to float.
    """

    currency = CurrencyField(
        _("Currency"),
        amount_fields=(
            "price",
            "price_with_tax",
        ),
        get_choices_func=get_currency_choices,
        cast_to=float,
    )

    class Meta:
        managed = False
        db_table = Product._meta.db_table
        verbose_name = _("Product proxy (cast_to=float)")
        verbose_name_plural = _("Product proxies (cast_to=float)")


class ProductProxyCastToDecimal(AbstractProduct):
    """A sort of a proxy model to Product.

    Casts amount in fractional units to decimal.
    """

    currency = CurrencyField(
        _("Currency"),
        amount_fields=(
            "price",
            "price_with_tax",
        ),
        get_choices_func=get_currency_choices_with_sign,
        cast_to=lambda __v: Decimal(str(__v)),
    )

    class Meta:
        managed = False
        db_table = Product._meta.db_table
        verbose_name = _("Product proxy (cast_to=decimal)")
        verbose_name_plural = _("Product proxies (cast_to=decimal)")


class ProductProxyLimitChoicesTo(AbstractProduct):
    """A sort of a proxy model to Product.

    Casts amount in fractional units to int.
    """

    currency = CurrencyField(
        _("Currency"),
        amount_fields=(
            "price",
            "price_with_tax",
        ),
        limit_choices_to=(
            valuta.EUR.uid,
            valuta.AMD.uid,
        ),
        get_choices_func=get_currency_choices_with_code,
    )

    class Meta:
        managed = False
        db_table = Product._meta.db_table
        verbose_name = _("Product proxy (limit_choices_to)")
        verbose_name_plural = _("Product proxies (limit_choices_to)")


class ProductProxyChoicesFuncNone(AbstractProduct):
    """A sort of a proxy model to Product.

    The `get_choices_func` argument is None here.
    """

    currency = CurrencyField(
        _("Currency"),
        amount_fields=(
            "price",
            "price_with_tax",
        ),
        limit_choices_to=(
            valuta.EUR.uid,
            valuta.AMD.uid,
        ),
        get_choices_func=None,
    )

    class Meta:
        managed = False
        db_table = Product._meta.db_table
        verbose_name = _("Product proxy (get_choices_func=None)")
        verbose_name_plural = _("Product proxies (get_choices_func=None)")
