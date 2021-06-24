from typing import Dict

from django.http import HttpRequest

from ...constants import (
    DISPLAY_FORMAT_NUMBER,
    DISPLAY_FORMAT_HUMAN_READABLE,
    DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE,
    DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL,
    DEFAULT_DISPLAY_FORMAT,
)

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("constants",)


def constants(request: HttpRequest) -> Dict[str, str]:
    return {
        "DISPLAY_FORMAT_NUMBER": DISPLAY_FORMAT_NUMBER,
        "DISPLAY_FORMAT_HUMAN_READABLE": DISPLAY_FORMAT_HUMAN_READABLE,
        "DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE": (
            DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE
        ),
        "DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL": (
            DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL
        ),
        "DEFAULT_DISPLAY_FORMAT": DEFAULT_DISPLAY_FORMAT,
    }
