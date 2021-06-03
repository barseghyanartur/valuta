import os
import tempfile
import unittest

from ..scaffolding import read_csv_and_write_output
from ..helpers import project_dir
from .data import LIST_GENERATED_CURRENCY_MODULES

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("TestScaffolding",)


class TestScaffolding(unittest.TestCase):
    """Scaffolding tests."""

    def test_generate_currencies(self):
        """Test generate currency modules."""
        out_dir = tempfile.mkdtemp()
        read_csv_and_write_output(out_dir=out_dir, skip_first_line=True)
        generated_modules = os.listdir(out_dir)
        generated_modules.sort()
        self.assertListEqual(
            LIST_GENERATED_CURRENCY_MODULES, generated_modules
        )

    def test_generate_currencies_rel_path(self):
        """Test generate currency modules relative paths."""
        os.makedirs(project_dir("var"), exist_ok=True)
        out_dir = read_csv_and_write_output(
            out_dir="var", skip_first_line=True
        )
        generated_modules = os.listdir(out_dir)
        generated_modules.sort()
        self.assertListEqual(
            LIST_GENERATED_CURRENCY_MODULES, generated_modules
        )
