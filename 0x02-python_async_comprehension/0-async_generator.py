#!usr/bin/env python3
"""
 Asynchronous Generator Module
 """

 import asyncio
 import random
 from typing import Generator

 async def async_generator() -> Generator[float, None, None]:
     '''
     Generates a sequence of 10 numbers.
      '''
      for _ in range(10):
          await asyncio.sleep(1)
          yield random.uniform(0, 10)

          def main():
               """Entry point for the script."""
               result = asyncio.run(async_generator())
                print(result)

                if __name__ == "__main__":
                    asyncio.run(main())
