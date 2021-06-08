import argparse
from functools import wraps, partial
import os
import subprocess
import sys
import time

import valuta
from valuta.shortcuts import convert_to_currency_units

path = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'benchmarks')

sys.path.insert(0, path)

from constants import CURRENCIES, TEST_CYCLES

try:
    if callable(profile):
        pass
except:
    from fallbacks import profile

REGISTRY = {}


def register(func):
    REGISTRY.update({func.__name__: func})

    def wrapper():
        func()
    return wrapper


@register
def python_classes():
    for _ in range(TEST_CYCLES):
        for currency_cls in CURRENCIES:
            currency_cls.convert_to_currency_units(1_000)


@register
def python_iso_string_representation():
    for _ in range(TEST_CYCLES):
        for currency_cls in CURRENCIES:
            convert_to_currency_units(currency_cls.uid, 1_000)


@register
def django_benchmark_product():
    res = subprocess.check_output(
        [
            "python",
            "examples/django_example/manage.py",
            "benchmark_product",
        ]
    ).strip()


@register
def django_benchmark_product_amount_fields_is_none():
    res = subprocess.check_output(
        [
            "python",
            "examples/django_example/manage.py",
            "benchmark_product_amount_fields_is_none",
        ]
    ).strip()


@profile
def main():
    parser = argparse.ArgumentParser(description="Profiling")
    parser.add_argument(
        "--func",
        dest="func",
        default=list(REGISTRY.keys())[0],
        action="store",
        help="Function to call",
        choices=list(REGISTRY.keys())
    )

    args = parser.parse_args(sys.argv[1:])
    func_name = args.func
    func = REGISTRY.get(func_name, None)

    if callable(func):
        print(f"Calling `{func_name}`")
        func()


if __name__ == "__main__":
    main()
