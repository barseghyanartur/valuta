from copy import deepcopy
import unittest

from ..base import BaseCurrency, Registry
from ..currencies import TND, EUR, MRU, VND, UGX
from ..exceptions import ImproperlyConfigured
from ..utils import get_currency_choices_with_code

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestBase",)


class TestBase(unittest.TestCase):
    """Base tests."""

    def setUp(self) -> None:
        self.registry_backup = deepcopy(Registry.REGISTRY)

    def tearDown(self) -> None:
        Registry.REGISTRY = self.registry_backup

    def test_subclass(self):
        """Test subclass."""

        class XYZ(BaseCurrency):
            """XYZ - Test currency."""

            uid: str = "XYZ"
            rate: int = 100_000_000

        self.assertIn(XYZ.uid, Registry.REGISTRY)
        self.assertEqual(XYZ.convert_to_currency_units(100_000_000), 1)

    def test_subclass_no_rate(self):
        """Test subclass no `rate`."""

        with self.assertRaises(ImproperlyConfigured):

            class CurrencyNoRate(BaseCurrency):
                uid: str = "XYZ"

    def test_symbol(self):
        """Test symbol."""
        self.assertEqual(Registry.get("EUR").symbol, "€")

    def test_1(self):
        self.assertEqual(UGX.convert_to_currency_units(10), 10)
        self.assertEqual(UGX.convert_to_currency_units(1_000), 1_000)

    def test_5(self):
        self.assertEqual(MRU.convert_to_currency_units(5), 1)
        self.assertEqual(MRU.convert_to_currency_units(1_000), 200)

    def test_10(self):
        self.assertEqual(VND.convert_to_currency_units(10), 1)
        self.assertEqual(VND.convert_to_currency_units(1_000), 100)

    def test_100(self):
        self.assertEqual(EUR.convert_to_currency_units(100), 1)
        self.assertEqual(EUR.convert_to_currency_units(1_000), 10)

    def test_1000(self):
        self.assertEqual(TND.convert_to_currency_units(1_000), 1)


class TestRegistry(unittest.TestCase):
    """Test registry."""

    def setUp(self) -> None:
        self.registry_backup = deepcopy(Registry.REGISTRY)

    def tearDown(self) -> None:
        Registry.REGISTRY = self.registry_backup

    def test_get_currency_choices(self):
        """Test Registry.reset."""
        Registry.reset()
        choices = get_currency_choices_with_code()
        self.assertListEqual(choices, [])

    def test_registry_items(self):
        items = Registry.items()
        choices = get_currency_choices_with_code()
        self.assertEqual(len(items), len(choices))
