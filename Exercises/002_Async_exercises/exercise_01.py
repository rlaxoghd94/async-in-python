"""
Exercise 1

Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay
"""
import asyncio


async def print_async():
    await asyncio.sleep(2)
    print('Python Exercises!')


async def main():
    await print_async()


if __name__ == '__main__':
    asyncio.run(main())
