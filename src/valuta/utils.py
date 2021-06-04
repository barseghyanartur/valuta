from typing import Tuple, List, Set, Union
from .base import Registry

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "get_currency_choices",
    "get_currency_choices_with_code",
)


def get_currency_choices(
    limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
    sort_by_key: bool = False,
) -> List[Tuple[str, str]]:
    """Get currency choices.

    List of choices in the following format::

        [
            ("AMD", "Armenian Dram"),
            ("EUR", "Euro"),
        ]
    """
    return Registry.values(limit_choices_to, sort_by_key)


def get_currency_choices_with_code(
    limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
    sort_by_key: bool = False,
) -> List[Tuple[str, str]]:
    """Get currency choices with code.

    List of choices in the following format::

        [
            ("AMD", "Armenian Dram (AMD)"),
            ("EUR", "Euro (EUR)"),
        ]
    """
    return Registry.values_with_code(limit_choices_to, sort_by_key)
