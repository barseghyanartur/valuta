from functools import partialmethod
from typing import Union, List, Tuple, Optional, Set, Callable

from django.db import models
from django.db.models import (
    IntegerField,
    BigIntegerField,
    SmallIntegerField,
    FloatField,
)
from django.conf import settings

from ...base import Registry
from ...constants import DEFAULT_DISPLAY_FORMAT
from ...utils import get_currency_choices_with_code

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("CurrencyField",)


class CurrencyField(models.CharField):
    """Currency field."""

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
        self.amount_fields = amount_fields
        self.cast_to = cast_to
        if get_choices_func is None:
            get_choices_func = get_currency_choices_with_code
        kwargs["max_length"] = 10
        if limit_choices_to is None:
            settings_limit_choices_to = getattr(
                settings, "VALUTA_FIELD_LIMIT_CHOICES_TO", None
            )
            if settings_limit_choices_to:
                limit_choices_to = settings_limit_choices_to

        kwargs["choices"] = get_choices_func(limit_choices_to)
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)
        if not self.null:
            setattr(
                cls,
                f"get_currency_cls_for_{self.name}",
                partialmethod(self.__class__._get_currency_cls, field=self),
            )
            if self.amount_fields:
                for amount_field in self.amount_fields:
                    # Set `_in_currency_units`
                    setattr(
                        cls,
                        f"{amount_field}_in_currency_units",
                        partialmethod(
                            self.__class__._convert_to_currency_units,
                            field=self,
                            amount_field=amount_field,
                        ),
                    )
                    # Set `_display_in_currency_units`
                    setattr(
                        cls,
                        f"{amount_field}_display_in_currency_units",
                        partialmethod(
                            self.__class__._display_in_currency_units,
                            field=self,
                            amount_field=amount_field,
                        ),
                    )

    def _get_currency_cls(
        self,
        field: Union[
            IntegerField, BigIntegerField, SmallIntegerField, FloatField
        ],
        **kwargs,
    ):
        key = getattr(self, field.name)
        if not key:
            return None
        return Registry.get(key)

    def _convert_to_currency_units(
        self,
        field: "CurrencyField",
        amount_field: str,
        **kwargs,
    ):
        key = getattr(self, field.name)
        if not key:
            return None
        currency_cls = Registry.get(key)
        if currency_cls is None:
            return None
        amount_in_fractional_units = getattr(self, amount_field)
        value = currency_cls.convert_to_currency_units(
            amount_in_fractional_units
        )
        if field.cast_to:
            return field.cast_to(value)
        return value

    def _display_in_currency_units(
        self,
        field: "CurrencyField",
        amount_field: str,
        format: Optional[str] = DEFAULT_DISPLAY_FORMAT,
        locale: Optional[str] = None,
        decimal_quantization: bool = True,
        **kwargs,
    ):
        key = getattr(self, field.name)
        if not key:
            return None
        currency_cls = Registry.get(key)
        if currency_cls is None:
            return None
        amount_in_fractional_units = getattr(self, amount_field)
        value = currency_cls.display_in_currency_units(
            amount_in_fractional_units, format, locale, decimal_quantization
        )
        return value
