from importlib import import_module
from inspect import isclass
import os
from pkgutil import iter_modules

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"


# Iterate through the modules in the current package
package_dir = os.path.dirname(__file__)

__all = []

for (_, module_name, _) in iter_modules([package_dir]):

    # Import the module and iterate through its attributes
    module = import_module(f"{__name__}.{module_name}")
    __all.extend(getattr(module, "__all__"))
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        if isclass(attribute):
            # Add the class to this package's variables
            globals()[attribute_name] = attribute

__all__ = tuple(__all)
