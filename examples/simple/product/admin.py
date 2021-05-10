from django.contrib import admin

from .models import Product, ProductProxyLimitChoicesTo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "price_with_tax",
        "currency",
    )


@admin.register(ProductProxyLimitChoicesTo)
class ProductProxyLimitChoicesToAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "price_with_tax",
        "currency",
    )
