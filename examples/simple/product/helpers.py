import operator
from typing import List, Tuple, Set, Union

from babel.numbers import get_currency_symbol
from valuta.registry import Registry

__all__ = ("get_currency_choices_with_sign",)


def get_currency_choices_with_sign(
    limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
    sort_by_key: bool = False,
) -> List[Tuple[str, str]]:
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
