#!/usr/bin/env python3
""" async_comprehension coroutine """

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return random numbers using an async comprehensing """
    random_nums = [random async for random in async_generator()]
    return random_nums
