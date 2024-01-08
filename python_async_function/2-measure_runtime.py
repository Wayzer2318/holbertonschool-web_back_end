#!/usr/bin/env python3
"""async"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """async"""
    start = time.process_time()
    asyncio.run(wait_n(n, max_delay))
    end = time.process_time()
    return (end - start) / n
