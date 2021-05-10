from ..base import BaseCurrency

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("THB",)


class THB(BaseCurrency):
    """THB - Thai baht."""

    uid: str = "THB"
    rate: int = 100
