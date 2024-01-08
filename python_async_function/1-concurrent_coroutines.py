#!/usr/bin/env python3
"""async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async"""
    results: List[float] = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]
    return [await result for result in asyncio.as_completed(results)]
