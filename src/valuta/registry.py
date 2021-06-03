import warnings
from .base import Registry

warnings.warn(
    "The `Registry` class is moved from `valuta.registry` to `valuta.base`.",
    DeprecationWarning,
)

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("Registry",)
