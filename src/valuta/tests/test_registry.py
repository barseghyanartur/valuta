from copy import deepcopy
import logging
import unittest

from ..utils import get_currency_choices_with_code
from ..registry import Registry

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestRegistry",)

LOGGER = logging.getLogger(__name__)


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
