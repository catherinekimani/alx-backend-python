#!/usr/bin/env python3
""" measure_runtime coroutine """

import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    start = time.perf_counter()
    coroutines = []
    for idx in range(4):
        coroutines.append(async_comprehension())
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return end - start
