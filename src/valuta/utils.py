from typing import Tuple, List, Set, Union
from .base import BaseCurrency
from .registry import Registry

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("get_currency_choices",)


def get_currency_choices(
    limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
    sort_by_key: bool = False,
) -> List[Tuple[str, BaseCurrency]]:
    """Get currency choices."""
    return Registry.values(limit_choices_to, sort_by_key)
