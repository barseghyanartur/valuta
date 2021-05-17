from copy import deepcopy
import unittest

from ..base import BaseCurrency
from ..exceptions import ImproperlyConfigured
from ..registry import Registry

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


if __name__ == "__main__":
    unittest.main()
