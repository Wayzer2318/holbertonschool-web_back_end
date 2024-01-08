#!/usr/bin/env python3
"""Asyn"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """sync"""
    return asyncio.create_task(wait_random(max_delay))
