"""
Exercise 2

Write a Python program that creates three asynchronous functions and displays their respective names with
different delays(1s, 2s, 3s).
"""
import asyncio


async def sleep_async(name: str, seconds: int):
    await asyncio.sleep(seconds)
    print(f'[sleep_async] {name}, seconds: {seconds}')


async def main():
    tasks = [
        sleep_async("fun1", 1),
        sleep_async("fun2", 2),
        sleep_async("fun3", 3),
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
