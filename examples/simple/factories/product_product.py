from factory import LazyAttribute, Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from valuta.utils import get_currency_choices

from product.models import Product

__all__ = ("ProductFactory",)


class BaseProductFactory(DjangoModelFactory):
    """Base product factory."""

    name = Faker("text", max_nb_chars=100)
    price = Faker("pyint", min_value=100, max_value=1_000_000)
    price_with_tax = LazyAttribute(lambda __x: int(__x.price * 1.20))
    currency = FuzzyChoice([key for key, value in get_currency_choices()])

    class Meta:
        """Meta class."""

        model = Product
        abstract = True


class ProductFactory(BaseProductFactory):
    """Product factory."""
