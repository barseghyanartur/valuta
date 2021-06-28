from decimal import Decimal
import operator
from typing import Optional, Dict, Union, List, Set, Tuple, ItemsView
from babel.numbers import (
    get_currency_name,
    get_currency_symbol,
    format_currency,
)

from .constants import DEFAULT_DISPLAY_FORMAT
from .exceptions import ImproperlyConfigured
from .helpers import classproperty

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "BaseCurrency",
    "Registry",
)


class Registry(type):
    REGISTRY: Dict[str, "BaseCurrency"] = {}

    def __new__(mcs, name, bases, attrs):
        new_cls = type.__new__(mcs, name, bases, attrs)
        # Here the name of the class is used as key but it could be any class
        # parameter.
        if getattr(new_cls, "_uid", None):
            mcs.REGISTRY[new_cls._uid] = new_cls
        if new_cls.__name__ != "BaseCurrency":
            new_cls.validate()
        return new_cls

    @property
    def _uid(cls) -> str:
        return getattr(cls, "uid", cls.__name__)

    @classmethod
    def reset(mcs) -> None:
        mcs.REGISTRY = {}

    @classmethod
    def get(
        mcs, key: str, default: "BaseCurrency" = None
    ) -> Union["BaseCurrency", None]:
        return mcs.REGISTRY.get(key, default)

    @classmethod
    def items(mcs) -> ItemsView[str, "BaseCurrency"]:
        return mcs.REGISTRY.items()

    @classmethod
    def values(
        mcs,
        limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
        sort_by_key: bool = False,
    ) -> List[Tuple[str, str]]:
        if limit_choices_to is None:
            values = [
                (__key, __value.name)
                for __key, __value in mcs.REGISTRY.items()
            ]
        else:
            values = [
                (__key, __value.name)
                for __key, __value in mcs.REGISTRY.items()
                if __key in limit_choices_to
            ]
        if sort_by_key:
            values.sort(key=operator.itemgetter(0))
        else:
            values.sort(key=operator.itemgetter(1))
        return values

    @classmethod
    def values_with_code(
        mcs,
        limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
        sort_by_key: bool = False,
    ) -> List[Tuple[str, str]]:
        if limit_choices_to is None:
            values = [
                (__key, f"{__value.name} ({__key})")
                for __key, __value in mcs.REGISTRY.items()
            ]
        else:
            values = [
                (__key, f"{__value.name} ({__key})")
                for __key, __value in mcs.REGISTRY.items()
                if __key in limit_choices_to
            ]
        if sort_by_key:
            values.sort(key=operator.itemgetter(0))
        else:
            values.sort(key=operator.itemgetter(1))
        return values


class BaseCurrency(metaclass=Registry):
    """Base currency.

    Each currency typically has a main currency unit (the dollar, for
    example, or the euro) and a fractional unit, often defined as 1⁄100 of
    the main unit: 100 cents = 1 dollar, 100 centimes = 1 franc,
    100 pence = 1 pound, although units of 1⁄10 or 1⁄1000 occasionally also
    occur. Some currencies do not have any smaller units at all, such as the
    Icelandic krona.

    https://en.wikipedia.org/wiki/Currency
    """

    uid: Optional[str] = None
    rate: Union[int, float, Decimal]

    @classmethod
    def validate(cls):
        """Constructor."""
        if not hasattr(cls, "rate"):
            raise ImproperlyConfigured(
                "The `rate` property of the currency shall be defined."
            )

    @classmethod
    def convert_to_currency_units(
        cls, value: int
    ) -> Union[int, float, Decimal]:
        """Convert to amount in currency units."""
        return value / cls.rate

    @classmethod
    def display_in_currency_units(
        cls,
        value: int,
        format: Optional[str] = DEFAULT_DISPLAY_FORMAT,
        locale: Optional[str] = None,
        decimal_quantization: bool = True,
    ) -> str:
        """Convert to amount in currency units."""
        kwargs = {}
        if locale is not None:
            kwargs = {"locale": locale}
        return format_currency(
            value / cls.rate,
            cls.uid,
            format,
            decimal_quantization=decimal_quantization,
            **kwargs,
        )

    @classproperty
    def name(cls) -> str:
        """Automatic currency name.

        Example::

            from babel.numbers import get_currency_name
            In: get_currency_name('AMD')
            Out: 'Armenian Dram'

            In: get_currency_name('AMD', locale='hy_AM')
            Out: 'հայկական դրամ'

            In: get_currency_name('AMD', locale='nl_NL')
            Out: 'Armeense dram'

        :return:
        """
        return get_currency_name(cls.uid)

    @classproperty
    def symbol(cls) -> str:
        """Automatic currency symbol.

        Example::

            from babel.numbers import get_currency_symbol
            In: get_currency_symbol('AMD')
            Out: 'AMD'

            In: get_currency_symbol('AMD', locale='hy_AM')
            Out: '֏'

            In: get_currency_symbol('AMD', locale='nl_NL')
            Out: 'AMD'

        :return:
        """
        return get_currency_symbol(cls.uid)
