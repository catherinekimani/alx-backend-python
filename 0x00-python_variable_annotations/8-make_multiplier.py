#!/usr/bin/env python3
""" Type annotation func make_multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a func that multiplies a float by the given multiplier."""
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
