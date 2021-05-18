from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

import valuta
from valuta.contrib.django_integration.models import CurrencyField

__all__ = (
    "Product",
    "ProductProxyCastToInt",
    "ProductProxyCastToFloat",
    "ProductProxyCastToDecimal",
    "ProductProxyLimitChoicesTo",
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
        )
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
    )

    class Meta:
        managed = False
        db_table = Product._meta.db_table
        verbose_name = _("Product proxy (limit_choices_to)")
        verbose_name_plural = _("Product proxies (limit_choices_to)")
