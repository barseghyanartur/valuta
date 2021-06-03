import subprocess
import tempfile
import unittest

from .data import (
    LIST_CURRENCIES_OUTPUT,
    LIST_CURRENCIES_OUTPUT_SORTED_BY_VALUE,
)

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestCLI",)


class TestCLI(unittest.TestCase):
    """CLI tests."""

    def test_generate_currencies(self):
        """Test generate currencies CLI."""
        out_dir = tempfile.mkdtemp()
        res = subprocess.check_output(
            [
                "valuta-generate-currencies",
                "--out-dir",
                out_dir,
                "--skip-first-line",
            ]
        ).strip()
        self.assertEqual(res, b"")
        return res

    def test_list_currencies(self):
        """Test list currencies CLI."""
        res = subprocess.check_output(
            [
                "valuta-list-currencies",
            ]
        ).strip()
        self.assertEqual(res, LIST_CURRENCIES_OUTPUT)
        return res

    def test_list_currencies_sort_by_value(self):
        """Test list currencies CLI, sorted byvalue."""
        res = subprocess.check_output(
            [
                "valuta-list-currencies",
                "--sort-by-value",
            ]
        ).strip()
        self.assertEqual(res, LIST_CURRENCIES_OUTPUT_SORTED_BY_VALUE)
        return res
