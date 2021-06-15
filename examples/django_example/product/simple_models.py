from typing import Dict

from django.template.loader import render_to_string

__all__ = ("SimpleProduct",)


class SimpleProduct:

    currency_code: str
    price: int
    price_with_tax: int

    def __init__(self, currency_code: str, price: int, price_with_tax: int):
        self.currency_code = currency_code
        self.price = price
        self.price_with_tax = price_with_tax

    def get_context(self) -> Dict[str, "SimpleProduct"]:
        return {"instance": self}

    def filter_product_price_in_currency_units(self) -> str:
        return render_to_string(
            "product/filter_price_in_currency_units.html", self.get_context()
        )

    def filter_product_price_with_tax_in_currency_units(self) -> str:
        return render_to_string(
            "product/filter_price_with_tax_in_currency_units.html",
            self.get_context(),
        )

    def tag_product_price_in_currency_units(self) -> str:
        return render_to_string(
            "product/tag_price_in_currency_units.html", self.get_context()
        )

    def tag_product_price_with_tax_in_currency_units(self) -> str:
        return render_to_string(
            "product/tag_price_with_tax_in_currency_units.html",
            self.get_context(),
        )
