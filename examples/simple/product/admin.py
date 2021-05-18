from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Product, ProductProxyLimitChoicesTo


class ProductAdminMixin:
    """Product admin mixin."""

    @admin.display(description=_("Price in currency units"),
                   ordering="price")
    def display_price_in_currency_units(self, obj):
        return obj.price_in_currency_units()

    @admin.display(description=_("Price with tax in currency units"),
                   ordering="price_with_tax")
    def display_price_with_tax_in_currency_units(self, obj):
        return obj.price_with_tax_in_currency_units()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ProductAdminMixin):
    list_display = (
        "name",
        "price",
        "price_with_tax",
        "currency",
        "display_price_in_currency_units",
        "display_price_with_tax_in_currency_units",
    )


@admin.register(ProductProxyLimitChoicesTo)
class ProductProxyLimitChoicesToAdmin(admin.ModelAdmin, ProductAdminMixin):
    list_display = (
        "name",
        "price",
        "price_with_tax",
        "currency",
        "display_price_in_currency_units",
        "display_price_with_tax_in_currency_units",
    )
