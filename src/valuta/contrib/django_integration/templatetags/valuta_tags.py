from decimal import Decimal
from typing import Union, Optional

from django import template

from ....constants import DEFAULT_DISPLAY_FORMAT
from ....shortcuts import convert_to_currency_units, display_in_currency_units

register = template.Library()

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "filter_convert_to_currency_units",
    "tag_convert_to_currency_units",
    "filter_display_in_currency_units",
    "tag_display_in_currency_units",
)


@register.filter(name="convert_to_currency_units")
def filter_convert_to_currency_units(
    value: int, currency_code: str
) -> Union[int, float, Decimal, None]:
    return convert_to_currency_units(currency_code, value)


@register.simple_tag(name="convert_to_currency_units")
def tag_convert_to_currency_units(
    value: int, currency_code: str
) -> Union[int, float, Decimal, None]:
    return convert_to_currency_units(currency_code, value)


@register.filter(name="display_in_currency_units")
def filter_display_in_currency_units(
    value: int,
    currency_code: str,
    format: Optional[str] = DEFAULT_DISPLAY_FORMAT,
    locale: Optional[str] = None,
    decimal_quantization: bool = True,
) -> Union[str, None]:
    return display_in_currency_units(
        currency_code, value, format, locale, decimal_quantization
    )


@register.simple_tag(name="display_in_currency_units")
def tag_display_in_currency_units(
    value: int,
    currency_code: str,
    format: Optional[str] = DEFAULT_DISPLAY_FORMAT,
    locale: Optional[str] = None,
    decimal_quantization: bool = True,
) -> Union[str, None]:
    return display_in_currency_units(
        currency_code, value, format, locale, decimal_quantization
    )
