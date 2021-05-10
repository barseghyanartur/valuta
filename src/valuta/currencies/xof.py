from ..base import BaseCurrency

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("XOF",)


class XOF(BaseCurrency):
    """XOF - West African CFA franc."""

    uid: str = "XOF"
    rate: int = 100
