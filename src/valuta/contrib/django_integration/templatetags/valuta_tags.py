from decimal import Decimal
from typing import Union

from django import template

from ....shortcuts import convert_to_currency_units

register = template.Library()

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "filter_convert_to_currency_units",
    "tag_convert_to_currency_units",
)


@register.filter(name="convert_to_currency_units")
def filter_convert_to_currency_units(
    value: int, currency_code: str
) -> Union[int, float]:
    return convert_to_currency_units(currency_code, value)


@register.simple_tag(name="convert_to_currency_units")
def tag_convert_to_currency_units(
    value: int, currency_code: str
) -> Union[int, float, Decimal]:
    return convert_to_currency_units(currency_code, value)
