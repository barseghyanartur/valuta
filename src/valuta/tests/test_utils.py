import unittest

from ..utils import get_currency_choices, get_currency_choices_with_code
from .data import (
    CURRENCY_CHOICES,
    CURRENCY_CHOICES_SORT_BY_KEY,
    CURRENCY_CHOICES_WITH_CODE,
    CURRENCY_CHOICES_WITH_CODE_SORT_BY_KEY,
)

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestUtils",)


class TestUtils(unittest.TestCase):
    """Test utils."""

    def setUp(self):
        """Set up."""

    def test_get_currency_choices(self):
        """Test get_currency_choices."""
        choices = get_currency_choices()
        self.assertListEqual(choices, CURRENCY_CHOICES)

    def test_get_currency_choices_sort_by_key(self):
        """Test get_currency_choices sort_by_key=True."""
        choices = get_currency_choices(sort_by_key=True)
        self.assertListEqual(choices, CURRENCY_CHOICES_SORT_BY_KEY)

    def test_get_currency_choices_with_code(self):
        """Test get_currency_choices_with_code."""
        choices = get_currency_choices_with_code()
        self.assertListEqual(choices, CURRENCY_CHOICES_WITH_CODE)

    def test_get_currency_choices_with_code_sort_by_key(self):
        """Test get_currency_choices_with_code sort_by_key=True."""
        choices = get_currency_choices_with_code(sort_by_key=True)
        self.assertListEqual(choices, CURRENCY_CHOICES_WITH_CODE_SORT_BY_KEY)
