from decimal import Decimal
from typing import Union

from .base import Registry
from .exceptions import InvalidCurrency

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("convert_to_currency_units",)


def convert_to_currency_units(
    currency_code: str, value: int, fail_silently: bool = True
) -> Union[int, float, Decimal, None]:
    """Convert value represented in minor currency to major currency units."""
    cls = Registry.get(currency_code)
    if cls:
        return cls.convert_to_currency_units(value)
    elif not fail_silently:
        raise InvalidCurrency(
            f"Invalid or empty currency code: {currency_code}"
        )
