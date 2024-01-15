#!/usr/bin/env python3
""" multiple coroutines at the same time with async """
import asyncio
import random


from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine to spawn wait_random n times with specifies max_delay
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    output = await asyncio.gather(*coroutines)
    return output
