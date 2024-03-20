import asyncio


# define a coroutine
async def custom_coro():
    # await another coroutine
    await asyncio.sleep(1)


# main coroutine
async def main():
    # execute `custom_coro()` coroutine
    await custom_coro()


if __name__ == '__main__':
    # start the coroutine program
    asyncio.run(main())
