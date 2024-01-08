#!/usr/bin/env python3
"""functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Write a function that takes a float
    as argument and returns a function that multiplies a float
    by multiplier"""
    def multi(num: float) -> float:
        """multi: function that multiplies num by multiplier"""
        return num * multiplier

    return multi
