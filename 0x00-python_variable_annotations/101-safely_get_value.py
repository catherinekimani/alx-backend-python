#!/usr/bin/env python3
""" Duck typing annotation """
from typing import TypeVar, Mapping, Union, Any


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[T, Any]:
    """
    Safely retrieve a value from a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
