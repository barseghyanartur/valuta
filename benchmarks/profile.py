import os
import sys

import valuta

path = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'benchmarks')

sys.path.insert(0, path)

from constants import CURRENCIES, TEST_CYCLES

try:
    if callable(profile):
        pass
except:
    from fallbacks import profile


@profile
def main():
    for _ in range(TEST_CYCLES):
        for currency_cls in CURRENCIES:
            currency_cls.convert_to_currency_units(1_000)


if __name__ == '__main__':
    main()
