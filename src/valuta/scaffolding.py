import csv
import os.path

from .helpers import project_dir

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "generate_contents",
    "read_csv_and_write_output",
)


def generate_contents(
    iso_code: str,
    number_to_basic: str,
    currency: str,
) -> str:
    """Generate the contents for the given currency."""

    return f'''from ..base import BaseCurrency

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("{iso_code}",)


class {iso_code}(BaseCurrency):
    """{iso_code} - {currency}."""

    uid: str = "{iso_code}"
    rate: int = {number_to_basic}
'''


def read_csv_and_write_output(
    in_file: str = "list_of_circulating_currencies.csv",
    out_dir: str = "currencies",
    skip_first_line: bool = False,
) -> str:
    """Read CSV."""
    if not os.path.isabs(in_file):
        in_file = project_dir(in_file)

    if not os.path.isabs(out_dir):
        out_dir = project_dir(out_dir)

    processed = set([])
    with open(in_file) as csv_file:
        reader = csv.reader(csv_file)
        if skip_first_line:
            next(reader)

        for row in reader:
            currency = row[1].strip()
            iso_code = row[3].strip()
            number_to_basic = row[5].strip()

            if "none" in iso_code:
                continue

            if "none" in number_to_basic:
                number_to_basic = "1"

            iso_code = iso_code[:3]

            if iso_code not in processed:
                contents = generate_contents(
                    iso_code, number_to_basic, currency
                )
                with open(f"{out_dir}/{iso_code.lower()}.py", "w") as output:
                    output.write(contents)
                    processed.add(iso_code)

    return out_dir
