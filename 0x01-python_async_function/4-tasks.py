#!/usr/bin/env python3
""" task_wait_n """

import asyncio
import random


from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task_wait_n """
    coroutines = []
    for _ in range(n):
        coroutines.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*coroutines))
