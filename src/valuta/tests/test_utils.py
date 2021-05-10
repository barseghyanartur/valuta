import logging
import unittest

from ..utils import get_currency_choices
from .data import CURRENCY_CHOICES

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestUtils",)

LOGGER = logging.getLogger(__name__)


class TestUtils(unittest.TestCase):
    """Test utils."""

    def setUp(self):
        """Set up."""

    def test_get_currency_choices(self):
        """Test get_currency_choices."""
        choices = get_currency_choices()
        self.assertListEqual(choices, CURRENCY_CHOICES)


if __name__ == "__main__":
    unittest.main()
