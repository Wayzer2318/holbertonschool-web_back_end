#!/usr/bin/env python3
"""string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Write a function to_kv that takes a string and an int
    OR float as arguments and returns a tuple"""
    vSquare = (v * v)
    result: Tuple[str, float] = (k, vSquare)
    return result
