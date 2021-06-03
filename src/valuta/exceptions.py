__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "ImproperlyConfigured",
    "InvalidCurrency",
)


class ImproperlyConfigured(Exception):
    """ImproperlyConfigured.

    Supposed to be thrown when code is improperly configured.
    """


class InvalidCurrency(ValueError):
    """Invalid currency exception."""
