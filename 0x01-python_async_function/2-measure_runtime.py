#!/usr/bin/env python3
import time
import asyncio

# Import the wait_n function from the previous task
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
     """Measures the total execution time for wait_n and returns average time"""
      start = time.time()  # Start measuring time using time.time()
       asyncio.run(wait_n(n, max_delay))  # Execute the wait_n function
        end = time.time()  # End measuring time
        total_time = end - start  # Calculate the total time
        return total_time / n  # Return average time per coroutine
