#!/usr/bin/env python3

"""
 Let's execute multiple coroutines at the same time with async
 """

 import asyncio
 from typing import List

 wait_random = __import__('0-basic_async_syntax').wait_random
 async def wait_n(n: int, max_delay: int) -> float:
      """spawns wait_random n times with max_delay"""
      delays = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
      return sorted(delays)
