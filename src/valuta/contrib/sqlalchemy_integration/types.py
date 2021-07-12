from typing import Union, List, Tuple, Optional, Set, Callable

from sqlalchemy_utils import ChoiceType
from sqlalchemy_utils.types.choice import Choice, ChoiceTypeImpl

from ...utils import get_currency_choices_with_code

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "CurrencyType",
    "ChoiceWithExtras",
    "ChoiceTypeWithExtrasImpl",
)


class ChoiceWithExtras(Choice):
    def __init__(self, code, value, amount_fields=None, cast_to=None):
        super().__init__(code, value)
        self.amount_fields = amount_fields
        self.cast_to = cast_to

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.code == other.code
        return other == self.code


class ChoiceTypeWithExtrasImpl(ChoiceTypeImpl):
    def __init__(self, choices, amount_fields=None, cast_to=None):
        self.amount_fields = amount_fields
        self.cast_to = cast_to
        super().__init__(choices)

    def _coerce(self, value):
        if value is None:
            return value
        if isinstance(value, ChoiceWithExtras):
            return value
        return ChoiceWithExtras(
            value,
            self.choices_dict[value],
            amount_fields=self.amount_fields,
            cast_to=self.cast_to,
        )

    def process_bind_param(self, value, dialect):
        if value and isinstance(value, ChoiceWithExtras):
            return value.code
        return value

    def process_result_value(self, value, dialect):
        if value and value in self.choices_dict:
            return ChoiceWithExtras(
                value,
                self.choices_dict[value],
                amount_fields=self.amount_fields,
                cast_to=self.cast_to,
            )
        return None


class CurrencyType(ChoiceType):
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

        self.internal_only = True

        self.amount_fields = amount_fields
        self.cast_to = cast_to
        if get_choices_func is None:
            get_choices_func = get_currency_choices_with_code
        kwargs["choices"] = get_choices_func(limit_choices_to)
        # super().__init__(*args, **kwargs)
        self.choices = tuple(kwargs["choices"])
        self.type_impl = ChoiceTypeWithExtrasImpl(
            amount_fields=amount_fields, cast_to=cast_to, **kwargs
        )
        if "impl" in kwargs and kwargs.get("impl"):
            self.impl = kwargs.get("impl")
