"""
Exercise 7

Write a Python program that implements a timeout for an asynchronous operation using `asyncio.wait_for()`.
"""
import asyncio


async def sleep_async(duration: int):
    print(f"[sleep_async] duration: {duration}")
    await asyncio.sleep(duration)


async def main():
    timeout = 1

    try:
        await asyncio.wait_for(sleep_async(10), timeout)
    except asyncio.TimeoutError:
        print('timeout error caught')


if __name__ == '__main__':
    asyncio.run(main())
