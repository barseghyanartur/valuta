__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "DEFAULT_DISPLAY_FORMAT",
    "DISPLAY_FORMAT_HUMAN_READABLE",
    "DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE",
    "DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL",
    "DISPLAY_FORMAT_NUMBER",
)

DISPLAY_FORMAT_NUMBER = "###0.00"  # Used to be default
DISPLAY_FORMAT_HUMAN_READABLE = "#,##0.00"
DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE = "¤¤ #,##0.00"
DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL = "¤ #,##0.00"
DEFAULT_DISPLAY_FORMAT = None
