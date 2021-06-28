from decimal import Decimal
from typing import Union, Optional

from .base import Registry, BaseCurrency
from .constants import DEFAULT_DISPLAY_FORMAT
from .exceptions import InvalidCurrency

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "convert_to_currency_units",
    "display_in_currency_units",
)


def convert_to_currency_units(
    currency_code: str,
    value: int,
    fail_silently: bool = True,
) -> Union[int, float, Decimal, None]:
    """Convert value represented in minor currency to major currency units."""
    cls: Optional[BaseCurrency] = Registry.get(currency_code)
    if cls:
        return cls.convert_to_currency_units(value)
    elif not fail_silently:
        raise InvalidCurrency(
            f"Invalid or empty currency code: {currency_code}"
        )


def display_in_currency_units(
    currency_code: str,
    value: int,
    format: Optional[str] = DEFAULT_DISPLAY_FORMAT,
    locale: Optional[str] = None,
    decimal_quantization: bool = True,
    fail_silently: bool = True,
) -> Union[str, None]:
    """Convert value represented in minor currency to major currency units."""
    cls: Optional[BaseCurrency] = Registry.get(currency_code)
    if cls:
        return cls.display_in_currency_units(
            value, format, locale, decimal_quantization
        )
    elif not fail_silently:
        raise InvalidCurrency(
            f"Invalid or empty currency code: {currency_code}"
        )
