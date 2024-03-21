"""
Exercise 3

Write a Python program that creates an asyncio event loop and runs a coroutine that prints numbers from 1 to 7 with
delay of 1 second each.
"""
import asyncio


async def print_no():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(i)


if __name__ == '__main__':
    asyncio.run(print_no())
