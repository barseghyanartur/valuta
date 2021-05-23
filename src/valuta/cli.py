import argparse
import sys

from .scaffolding import read_csv_and_write_output
from .utils import get_currency_choices

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "generate_currencies",
    "list_currencies",
)


def generate_currencies():
    """Generate currency modules."""
    parser = argparse.ArgumentParser(description="Generate currency modules")
    parser.add_argument(
        "--in-file",
        dest="in_file",
        default="list_of_circulating_currencies.csv",
        action="store",
        help="Input file",
    )
    parser.add_argument(
        "--out-dir",
        dest="out_dir",
        default="currencies",
        action="store",
        help="Output directory",
    )
    parser.add_argument(
        "--skip-first-line",
        dest="skip_first_line",
        default=False,
        action="store_true",
        help="Skip first line from the CSV?",
    )
    args = parser.parse_args(sys.argv[1:])
    in_file = args.in_file
    out_dir = args.out_dir
    skip_first_line = args.skip_first_line
    read_csv_and_write_output(in_file, out_dir, skip_first_line)


def list_currencies():
    """List currency modules."""
    parser = argparse.ArgumentParser(description="List currency modules")
    parser.add_argument(
        "--sort-by-value",
        dest="sort_by_value",
        default=False,
        action="store_true",
        help="Sort by value?",
    )
    args = parser.parse_args(sys.argv[1:])
    sort_by_key = not args.sort_by_value
    currencies = get_currency_choices(sort_by_key=sort_by_key)
    total = len(currencies)
    print("┌───────────┬──────────────────────────────────────────┐")
    print("│ ISO code  │ Currency                                 │")
    print("├───────────┼──────────────────────────────────────────┤")
    for counter, (iso_code, currency) in enumerate(currencies):
        print(f"│ {iso_code}       │ {currency}{' '*(41-len(currency))}│")
        if counter == total - 1:
            print("└───────────┴──────────────────────────────────────────┘")
        else:
            print("├───────────┼──────────────────────────────────────────┤")
