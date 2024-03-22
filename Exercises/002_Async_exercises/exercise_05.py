"""
Exercise 5

Write a Python program that runs multiple asynchronous tasks concurrently using `asyncio.gather()` and measure the
time taken.
"""
import asyncio


async def print_async(message: str, duration: int):
    await asyncio.sleep(duration)
    print(message)


async def main():
    tasks = [
        print_async("1", 1),
        print_async("2", 2),
        print_async("3", 3),
        print_async("4", 4),
        print_async("5", 5),
        print_async("6", 6),
    ]

    start = asyncio.get_running_loop().time()
    _ = await asyncio.gather(*tasks)
    end = asyncio.get_running_loop().time()
    duration = end - start

    print(f'`asyncio.gather(..)` duration is {duration}s')


if __name__ == '__main__':
    asyncio.run(main())
