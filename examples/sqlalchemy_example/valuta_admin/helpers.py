import operator
from typing import Union

from babel.numbers import get_currency_symbol

from valuta.base import Registry

__all__ = ("get_currency_choices_with_sign",)


def get_currency_choices_with_sign(
    limit_choices_to: Union[tuple[str, ...], list[str], set[str]] = None,
    sort_by_key: bool = False,
) -> list[tuple[str, str]]:
    """Get currency choices with code.

    List of choices in the following format::

        [
            ("AMD", "AMD - Armenian Dram"),
            ("EUR", "€ - Euro"),
            ("USD", "$ - US Dollar"),
        ]
    """
    if limit_choices_to is None:
        values = [
            (__key, f"{get_currency_symbol(__key)} - {__value.name}")
            for __key, __value in Registry.REGISTRY.items()
        ]
    else:
        values = [
            (__key, f"{get_currency_symbol(__key)} - {__value.name}")
            for __key, __value in Registry.REGISTRY.items()
            if __key in limit_choices_to
        ]
    if sort_by_key:
        values.sort(key=operator.itemgetter(0))
    else:
        values.sort(key=operator.itemgetter(1))
    return values
