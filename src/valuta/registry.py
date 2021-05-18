import operator
from typing import Dict, Union, List, Set, Tuple

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("Registry",)


class Registry(type):
    REGISTRY = {}  # type: Dict[str, Registry]

    def __new__(mcs, name, bases, attrs):
        new_cls = type.__new__(mcs, name, bases, attrs)
        # Here the name of the class is used as key but it could be any class
        # parameter.
        if getattr(new_cls, "_uid", None):
            mcs.REGISTRY[new_cls._uid] = new_cls
        if new_cls.__name__ != "BaseCurrency":
            new_cls.validate()
        return new_cls

    @property
    def _uid(cls) -> str:
        return getattr(cls, "uid", cls.__name__)

    @classmethod
    def reset(mcs) -> None:
        mcs.REGISTRY = {}

    @classmethod
    def get(mcs, key, default=None):
        return mcs.REGISTRY.get(key, default)

    @classmethod
    def items(mcs):
        return mcs.REGISTRY.items()

    @classmethod
    def values(
        mcs,
        limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
        sort_by_key: bool = False,
    ):
        if limit_choices_to is None:
            values = [
                (__key, __value.name)
                for __key, __value in mcs.REGISTRY.items()
            ]
        else:
            values = [
                (__key, __value.name)
                for __key, __value in mcs.REGISTRY.items()
                if __key in limit_choices_to
            ]
        if sort_by_key:
            values.sort(key=operator.itemgetter(0))
        else:
            values.sort(key=operator.itemgetter(1))
        return values

    @classmethod
    def values_with_code(
        mcs,
        limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
        sort_by_key: bool = False,
    ):
        if limit_choices_to is None:
            values = [
                (__key, f"{__value.name} ({__key})")
                for __key, __value in mcs.REGISTRY.items()
            ]
        else:
            values = [
                (__key, f"{__value.name} ({__key})")
                for __key, __value in mcs.REGISTRY.items()
                if __key in limit_choices_to
            ]
        if sort_by_key:
            values.sort(key=operator.itemgetter(0))
        else:
            values.sort(key=operator.itemgetter(1))
        return values
