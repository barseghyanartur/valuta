from typing import Dict

# from django.template import Template, Context
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

    def get_context(self, **kwargs) -> Dict[str, "SimpleProduct"]:
        context = {"instance": self}
        context.update(**kwargs)
        return context

    # ***********************************************************
    # *************** Convert to currency units *****************
    # ***********************************************************

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

    # ***********************************************************
    # *************** Display in currency units *****************
    # ***********************************************************

    def filter_product_price_display_in_currency_units(self) -> str:
        # template = Template(
        #     "{% load valuta_tags %}"
        #     "{{ "
        #     "instance.price|display_in_currency_units:instance.currency_code"
        #     " }}"
        # )
        # context = Context(self.get_context())
        # return template.render(context)
        return render_to_string(
            "product/filter_price_display_in_currency_units.html",
            self.get_context(),
        )

    def filter_product_price_with_tax_display_in_currency_units(self) -> str:
        return render_to_string(
            "product/filter_price_with_tax_display_in_currency_units.html",
            self.get_context(),
        )

    def tag_product_price_display_in_currency_units(self) -> str:
        # template = Template(
        #     "{% load valuta_tags %}"
        #     "{% "
        #     "display_in_currency_units instance.price instance.currency_code"
        #     " %}"
        # )
        # context = Context(self.get_context())
        # return template.render(context)
        return render_to_string(
            "product/tag_price_display_in_currency_units.html",
            self.get_context(),
        )

    def tag_product_price_with_tax_display_in_currency_units(self) -> str:
        return render_to_string(
            "product/tag_price_with_tax_display_in_currency_units.html",
            self.get_context(),
        )

    def tag_product_price_display_in_currency_units_with_locale(
        self, locale
    ) -> str:
        return render_to_string(
            "product/tag_price_display_in_currency_units_with_locale.html",
            self.get_context(locale=locale),
        )
