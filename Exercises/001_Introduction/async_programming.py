import asyncio


async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')


if __name__ == '__main__':
    asyncio.run(fn())
