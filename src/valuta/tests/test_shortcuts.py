import unittest

from ..constants import DISPLAY_FORMAT_HUMAN_READABLE, DISPLAY_FORMAT_NUMBER
from ..currencies import TND, EUR, MRU, VND, UGX
from ..exceptions import InvalidCurrency
from ..shortcuts import convert_to_currency_units, display_in_currency_units


__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestShortcuts",)


class TestShortcuts(unittest.TestCase):
    """Test shortcuts."""

    # ***********************************************************
    # *************** Convert to currency units *****************
    # ***********************************************************

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

    # ***********************************************************
    # *************** Display in currency units *****************
    # ***********************************************************

    def test_display_in_currency_units(self):
        """Test `display_in_currency_units` with valid codes."""
        self.assertEqual(
            display_in_currency_units(
                UGX.uid, 10, format=DISPLAY_FORMAT_NUMBER
            ),
            "10",
        )

        self.assertEqual(
            display_in_currency_units(
                MRU.uid, 5, format=DISPLAY_FORMAT_NUMBER
            ),
            "1.00",
        )

        self.assertEqual(
            display_in_currency_units(
                VND.uid, 10, format=DISPLAY_FORMAT_NUMBER
            ),
            "1",
        )

        self.assertEqual(
            display_in_currency_units(
                EUR.uid, 100, format=DISPLAY_FORMAT_NUMBER
            ),
            "1.00",
        )

        self.assertEqual(
            display_in_currency_units(
                TND.uid, 1_000, format=DISPLAY_FORMAT_NUMBER
            ),
            "1.000",
        )

    def test_display_in_currency_units_with_locale(self):
        """Test `display_in_currency_units` with valid codes and locale."""
        with self.subTest("EUR locale nl_NL"):
            self.assertEqual(
                display_in_currency_units(
                    EUR.uid,
                    100,
                    locale="nl_NL",
                ),
                "€\xa01,00",
            )

            self.assertEqual(
                display_in_currency_units(
                    EUR.uid,
                    100_000,
                    locale="nl_NL",
                ),
                "€\xa01.000,00",
            )

        with self.subTest("TND locale fr_TN"):
            self.assertEqual(
                display_in_currency_units(
                    TND.uid,
                    100,
                    locale="fr_TN",
                ),
                "0,100\xa0DT",
            )

            self.assertEqual(
                display_in_currency_units(
                    TND.uid,
                    1_000,
                    locale="fr_TN",
                ),
                "1,000\xa0DT",
            )

        with self.subTest("TND locale nl_NL"):
            self.assertEqual(
                display_in_currency_units(
                    TND.uid,
                    100,
                    locale="nl_NL",
                ),
                "TND\xa00,100",
            )

            self.assertEqual(
                display_in_currency_units(
                    TND.uid,
                    1_000,
                    locale="nl_NL",
                ),
                "TND\xa01,000",
            )

    def _display_test_currency_code_is_none(self, fail_silently: bool = True):
        self.assertEqual(
            display_in_currency_units(
                None, 1_000, fail_silently=fail_silently
            ),
            None,
        )

    def _display_test_currency_code_is_empty_string(
        self, fail_silently: bool = True
    ):
        self.assertEqual(
            display_in_currency_units("", 1_000, fail_silently=fail_silently),
            None,
        )

    def _display_test_currency_code_is_invalid(
        self, fail_silently: bool = True
    ):
        self.assertEqual(
            display_in_currency_units(
                "None", 1_000, fail_silently=fail_silently
            ),
            None,
        )

    def test_test_display_in_currency_units_invalid_currency_code(self):
        """Test `convert_to_currency_units` with invalid codes."""

        with self.subTest("currency_code=None"):
            self._display_test_currency_code_is_none()

        with self.subTest("currency_code=''"):
            self._display_test_currency_code_is_empty_string()

        with self.subTest("currency_code='None'"):
            self._display_test_currency_code_is_invalid()

        with self.assertRaises(InvalidCurrency):
            with self.subTest("currency_code=None"):
                self._display_test_currency_code_is_none(fail_silently=False)

        with self.assertRaises(InvalidCurrency):
            with self.subTest("currency_code=''"):
                self._display_test_currency_code_is_empty_string(
                    fail_silently=False
                )

        with self.assertRaises(InvalidCurrency):
            with self.subTest("currency_code='None'"):
                self._display_test_currency_code_is_invalid(
                    fail_silently=False
                )
