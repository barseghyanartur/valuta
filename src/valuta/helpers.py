import os

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "ClassProperty",
    "classproperty",
    "project_dir",
)


class ClassProperty(property):
    """ClassProperty.

    How to use::

        class Something:
            @classproperty
            def default_value(cls):
                return 10  # Some value

    Can be replaced with the following in Python 3.9::

        class Something:
            @classmethod
            @property
            def default_value(cls):
                return 10  # Some value
    """

    def __get__(self, cls, owner):
        """Get."""
        return classmethod(self.fget).__get__(None, owner)()


classproperty = ClassProperty


def project_dir(base: str) -> str:
    """Absolute path to a file from current directory."""
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), base).replace("\\", "/")
    )
