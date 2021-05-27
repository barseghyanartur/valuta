from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (
    Product,
    ProductProxyLimitChoicesTo,
    ProductProxyCastToInt,
    ProductProxyCastToFloat,
    ProductProxyCastToDecimal,
)

__all__ = (
    "ProductAdmin",
    "ProductProxyLimitChoicesToAdmin",
    "ProductProxyCastToIntAdmin",
    "ProductProxyCastToFloatAdmin",
    "ProductProxyCastToDecimalAdmin",
)


class ProductAdminMixin:
    """Product admin mixin."""

    list_display = (
        "name",
        "price",
        "price_with_tax",
        "currency",
        "display_price_in_currency_units",
        "display_price_with_tax_in_currency_units",
    )

    def display_price_in_currency_units(self, obj):
        return obj.price_in_currency_units()

    display_price_in_currency_units.short_description = _(
        "Price in currency units"
    )
    display_price_in_currency_units.admin_order_field = "price"

    def display_price_with_tax_in_currency_units(self, obj):
        return obj.price_with_tax_in_currency_units()

    display_price_with_tax_in_currency_units.short_description = _(
        "Price with tax in currency units"
    )
    display_price_with_tax_in_currency_units.admin_order_field = (
        "price_with_tax"
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ProductAdminMixin):
    """Product admin."""

    list_display = ProductAdminMixin.list_display


@admin.register(ProductProxyLimitChoicesTo)
class ProductProxyLimitChoicesToAdmin(admin.ModelAdmin, ProductAdminMixin):
    """ProductProxyLimitChoicesTo admin."""

    list_display = ProductAdminMixin.list_display


@admin.register(ProductProxyCastToInt)
class ProductProxyCastToIntAdmin(admin.ModelAdmin, ProductAdminMixin):
    """ProductProxyCastToInt admin."""

    list_display = ProductAdminMixin.list_display


@admin.register(ProductProxyCastToFloat)
class ProductProxyCastToFloatAdmin(admin.ModelAdmin, ProductAdminMixin):
    """ProductProxyCastToFloat admin."""

    list_display = ProductAdminMixin.list_display


@admin.register(ProductProxyCastToDecimal)
class ProductProxyCastToDecimalAdmin(admin.ModelAdmin, ProductAdminMixin):
    """ProductProxyCastToDecimal admin."""

    list_display = ProductAdminMixin.list_display
