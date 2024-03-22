"""
Exercise 6

Write a Python program to create a coroutine that simulates a time-consuming task and use `asyncio.CancelledError` to
handle task cancellation.
"""
import asyncio


async def cancel_async(duration: int):
    print(f'[cancel_async] duration: {duration} start')
    try:
        await asyncio.sleep(duration)
    except asyncio.CancelledError:
        raise
    print(f'[cancel_async] duration: {duration} success')


async def main():
    task = asyncio.create_task(cancel_async(20))  # schedules(~=runs if possible) tasks
    await asyncio.sleep(2)  # this allows task to actually run in the first place. Without this, task won't event run
    task.cancel()
    try:
        await task
    except asyncio.CancelledError as ace:
        print('task2 failed with `asyncio.CancelledError`')


if __name__ == '__main__':
    asyncio.run(main())
