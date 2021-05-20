from ..base import BaseCurrency

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("SLS",)


class SLS(BaseCurrency):
    """SLS - Somaliland shilling."""

    uid: str = "SLS"
    rate: int = 100
