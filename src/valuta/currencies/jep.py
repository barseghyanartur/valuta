from ..base import BaseCurrency

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("JEP",)


class JEP(BaseCurrency):
    """JEP - Jersey pound."""

    uid: str = "JEP"
    rate: int = 100
