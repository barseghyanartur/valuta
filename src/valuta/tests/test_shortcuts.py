import unittest

from ..currencies import TND, EUR, MRU, VND, UGX
from ..exceptions import InvalidCurrency
from ..shortcuts import convert_to_currency_units


__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestShortcuts",)


class TestShortcuts(unittest.TestCase):
    """Test shortcuts."""

    def test_convert_to_currency_units(self):
        """Test `convert_to_currency_units` with valid codes."""
        self.assertEqual(convert_to_currency_units(UGX.uid, 10), 10)

        self.assertEqual(convert_to_currency_units(MRU.uid, 5), 1)

        self.assertEqual(convert_to_currency_units(VND.uid, 10), 1)

        self.assertEqual(convert_to_currency_units(EUR.uid, 100), 1)

        self.assertEqual(convert_to_currency_units(TND.uid, 1_000), 1)

    def _test_currency_code_is_none(self, fail_silently: bool = True):
        self.assertEqual(
            convert_to_currency_units(None, 1_000, fail_silently), None
        )

    def _test_currency_code_is_empty_string(self, fail_silently: bool = True):
        self.assertEqual(
            convert_to_currency_units("", 1_000, fail_silently), None
        )

    def _test_currency_code_is_invalid(self, fail_silently: bool = True):
        self.assertEqual(
            convert_to_currency_units("None", 1_000, fail_silently), None
        )

    def test_test_convert_to_currency_units_invalid_currency_code(self):
        """Test `convert_to_currency_units` with invalid codes."""

        with self.subTest("currency_code=None"):
            self._test_currency_code_is_none()

        with self.subTest("currency_code=''"):
            self._test_currency_code_is_empty_string()

        with self.subTest("currency_code='None'"):
            self._test_currency_code_is_invalid()

        with self.assertRaises(InvalidCurrency):
            with self.subTest("currency_code=None"):
                self._test_currency_code_is_none(fail_silently=False)

        with self.assertRaises(InvalidCurrency):
            with self.subTest("currency_code=''"):
                self._test_currency_code_is_empty_string(fail_silently=False)

        with self.assertRaises(InvalidCurrency):
            with self.subTest("currency_code='None'"):
                self._test_currency_code_is_invalid(fail_silently=False)
