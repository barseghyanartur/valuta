__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("ImproperlyConfigured",)


class ImproperlyConfigured(Exception):
    """ImproperlyConfigured.

    Supposed to be thrown when code is improperly configured.
    """

    def __init__(self, msg=None):
        if msg is None:
            msg = "Improperly configured."
        else:
            msg = "Improperly configured. %s" % msg

        super(ImproperlyConfigured, self).__init__(msg)
