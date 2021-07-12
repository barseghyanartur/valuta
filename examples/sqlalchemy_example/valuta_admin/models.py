from decimal import Decimal
import json
from typing import Union, Optional

import valuta
from valuta.base import Registry, BaseCurrency
from valuta.constants import DEFAULT_DISPLAY_FORMAT
from valuta.shortcuts import convert_to_currency_units
from valuta.utils import get_currency_choices, get_currency_choices_with_code
from valuta.contrib.sqlalchemy_integration.types import CurrencyType

from . import db
from .helpers import get_currency_choices_with_sign


__all__ = (
    "AbstractProduct",
    "Product",
    "ProductProxyCastToInt",
    "ProductProxyCastToFloat",
    "ProductProxyCastToDecimal",
    "ProductProxyLimitChoicesTo",
    "ProductProxyChoicesFuncNone",
    "ProductProxyAmountFieldsIsNone",
)


# def to_dict(self):
#     return json.loads(json.dumps(self, default=lambda o: o.__dict__))
#
#
# def dict_from_class(cls):
#     return dict((key, value) for (key, value) in cls.__dict__.items())


class AbstractProduct(db.Model):
    """Abstract product model."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), unique=True)
    price = db.Column(db.Integer())
    price_with_tax = db.Column(db.Integer())

    def __str__(self) -> str:
        return f"{self.name}"

    def get_currency_cls_for_currency(self) -> Union[BaseCurrency, None]:
        if not self.currency:
            return None
        return Registry.get(self.currency.code)

    def price_in_currency_units(self) -> Union[int, float, Decimal, None]:
        if not self.currency:
            return None

        value = convert_to_currency_units(self.currency.code, self.price)
        if self.currency.cast_to:
            return self.currency.cast_to(value)
        return value

    def price_with_tax_in_currency_units(
        self,
    ) -> Union[int, float, Decimal, None]:
        if not self.currency:
            return None

        value = convert_to_currency_units(
            self.currency.code, self.price_with_tax
        )
        if self.currency.cast_to:
            return self.currency.cast_to(value)
        return value

    def price_display_in_currency_units(
        self,
        format: Optional[str] = DEFAULT_DISPLAY_FORMAT,
        locale: Optional[str] = None,
        decimal_quantization: bool = True,
    ) -> str:
        if not self.currency:
            return None

        currency_cls = Registry.get(self.currency.code)
        if currency_cls is None:
            return None

        value = currency_cls.display_in_currency_units(
            self.price, format, locale, decimal_quantization
        )
        return value

    def price_with_tax_display_in_currency_units(
        self,
        format: Optional[str] = DEFAULT_DISPLAY_FORMAT,
        locale: Optional[str] = None,
        decimal_quantization: bool = True,
    ) -> str:
        if not self.currency:
            return None

        currency_cls = Registry.get(self.currency.code)
        if currency_cls is None:
            return None

        value = currency_cls.display_in_currency_units(
            self.price_with_tax, format, locale, decimal_quantization
        )
        return value


class Product(AbstractProduct):
    """Product model."""

    __tablename__ = "product"
    __table_args__ = {"extend_existing": True}

    currency = db.Column(
        CurrencyType(
            amount_fields=(
                "price",
                "price_with_tax",
            ),
            get_choices_func=get_currency_choices_with_code,
        )
    )


class ProductProxyCastToInt(AbstractProduct):
    """A sort of a proxy model to Product.

    Casts amount in fractional units to int.
    """

    __tablename__ = Product.__tablename__
    __table_args__ = {"extend_existing": True}

    currency = db.Column(
        CurrencyType(
            amount_fields=(
                "price",
                "price_with_tax",
            ),
            cast_to=int,
        )
    )


class ProductProxyCastToFloat(AbstractProduct):
    """A sort of a proxy model to Product.

    Casts amount in fractional units to float.
    """

    __tablename__ = Product.__tablename__
    __table_args__ = {"extend_existing": True}

    currency = db.Column(
        CurrencyType(
            amount_fields=(
                "price",
                "price_with_tax",
            ),
            get_choices_func=get_currency_choices,
            cast_to=float,
        )
    )


class ProductProxyCastToDecimal(AbstractProduct):
    """A sort of a proxy model to Product.

    Casts amount in fractional units to decimal.
    """

    __tablename__ = Product.__tablename__
    __table_args__ = {"extend_existing": True}

    currency = db.Column(
        CurrencyType(
            amount_fields=(
                "price",
                "price_with_tax",
            ),
            get_choices_func=get_currency_choices_with_sign,
            cast_to=lambda __v: Decimal(str(__v)),
        )
    )


class ProductProxyLimitChoicesTo(AbstractProduct):
    """A sort of a proxy model to Product.

    Casts amount in fractional units to int.
    """

    __tablename__ = Product.__tablename__
    __table_args__ = {"extend_existing": True}

    currency = db.Column(
        CurrencyType(
            amount_fields=(
                "price",
                "price_with_tax",
            ),
            limit_choices_to=(
                valuta.EUR.uid,
                valuta.AMD.uid,
            ),
            get_choices_func=get_currency_choices_with_code,
        )
    )


class ProductProxyChoicesFuncNone(AbstractProduct):
    """A sort of a proxy model to Product.

    The `get_choices_func` argument is None here.
    """

    __tablename__ = Product.__tablename__
    __table_args__ = {"extend_existing": True}

    currency = db.Column(
        CurrencyType(
            amount_fields=(
                "price",
                "price_with_tax",
            ),
            limit_choices_to=(
                valuta.EUR.uid,
                valuta.AMD.uid,
            ),
            get_choices_func=None,
        )
    )


class ProductProxyAmountFieldsIsNone(AbstractProduct):
    """A sort of a proxy model to Product.

    The `amount_fields` is None here. No magic functions. Just a currency
    field.
    """

    __tablename__ = Product.__tablename__
    __table_args__ = {"extend_existing": True}

    currency = db.Column(CurrencyType())
    #
    # def price_in_currency_units(self):
    #     return convert_to_currency_units(self.currency, self.price)
    #
    # def price_with_tax_in_currency_units(self):
    #     return convert_to_currency_units(self.currency, self.price_with_tax)
