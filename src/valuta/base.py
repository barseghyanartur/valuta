from decimal import Decimal
from typing import Optional, Union

from babel.numbers import get_currency_name, get_currency_symbol

from .exceptions import ImproperlyConfigured
from .helpers import classproperty
from .registry import Registry

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("BaseCurrency",)


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
    name: str
    rate: int

    @classmethod
    def validate(cls):
        """Constructor."""
        if not hasattr(cls, "rate"):
            raise ImproperlyConfigured(
                "The `rate` property of the currency shall be defined."
            )

    @classmethod
    def convert_to_currency_units(
        cls, value: Union[int, float, Decimal]
    ) -> Union[int, float, Decimal]:
        """Convert to amount in currency units."""
        return value / cls.rate

    @classproperty
    def name(cls):
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
    def symbol(cls):
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
