from decimal import Decimal

import valuta
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


class AbstractProduct(db.Model):
    """Abstract product model."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), unique=True)
    price = db.Column(db.Integer())
    price_with_tax = db.Column(db.Integer())
    # currency = db.Column(CurrencyType())

    def __str__(self):
        return f"{self.name}"

    def price_in_currency_units(self):
        return convert_to_currency_units(self.currency, self.price)

    def price_with_tax_in_currency_units(self):
        return convert_to_currency_units(self.currency, self.price_with_tax)


class Product(AbstractProduct):
    """Product model."""

    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}

    currency = db.Column(CurrencyType())
    #
    # def price_in_currency_units(self):
    #     return convert_to_currency_units(self.currency, self.price)
    #
    # def price_with_tax_in_currency_units(self):
    #     return convert_to_currency_units(self.currency, self.price_with_tax)
