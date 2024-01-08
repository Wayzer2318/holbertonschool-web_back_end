#!/usr/bin/env python3
"""list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function which takes a list of floats
    and returns the sum as a float"""
    result: float = 0
    for num in input_list:
        result += num
    return result
