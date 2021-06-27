from functools import partialmethod
from typing import Union, List, Tuple, Optional, Set, Callable

from sqlalchemy.types import TypeDecorator, String

from ...base import Registry
from ...constants import DEFAULT_DISPLAY_FORMAT
from ...utils import get_currency_choices_with_code

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("CurrencyType",)


class CurrencyType(TypeDecorator):
    impl = String

    cache_ok = True

    def __init__(
        self,
        *args,
        amount_fields: Optional[
            Union[List[str], Tuple[str, ...], Set[str]]
        ] = None,
        limit_choices_to: Optional[
            Union[List[str], Tuple[str, ...], Set[str]]
        ] = None,
        get_choices_func: Callable = get_currency_choices_with_code,
        cast_to: Optional[Callable] = None,
        **kwargs,
    ):

        # self.choices = tuple(choices)
        self.internal_only = True

        self.amount_fields = amount_fields
        self.cast_to = cast_to
        if get_choices_func is None:
            get_choices_func = get_currency_choices_with_code
        kwargs["max_length"] = 10
        kwargs["choices"] = get_choices_func(limit_choices_to)
        super().__init__(*args, **kwargs)
