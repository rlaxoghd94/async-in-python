"""
Exercise 4

Write a Python program that implements a coroutine to fetch data from two different URLs simultaneously
using "aiohttp" library.
"""
import asyncio
from typing import Union, List, Dict

import aiohttp


async def get_content_async(http_session: aiohttp.ClientSession, url: str) -> Union[List, Dict]:
    """
    fetch content via asynchronous HTTP Get

    :param aiohttp.ClientSession http_session: client session that contains connection pool managed by `aiohttp`
    :param str url: URL for asynchronous HTTP Get request
    :return: HTTP Get response json content
    :rtype: List or Dict
    """
    response = await http_session.get(url)
    content = await response.json()

    return content


def print_url_and_content(url: str, content: Union[List, Dict]):
    print(f'[+] request url: {url}\n{content}\n')


async def main():
    http_session = aiohttp.ClientSession()

    url1 = "http://httpbin.org/get"
    url2 = "https://api.github.com/events"

    task1 = asyncio.create_task(get_content_async(http_session, url1))
    task2 = asyncio.create_task(get_content_async(http_session, url2))

    content1 = await task1
    content2 = await task2

    print_url_and_content(url1, content1)
    print_url_and_content(url2, content2)

    """
    explicit session close must occur if you fetch a session via `http_session = aiohttp.ClientSession()`
    
    NOTE:
    Don’t create a session per request. Most likely you need a session per application which performs all requests together.
    More complex cases may require a session per site, e.g. one for Github and other one for Facebook APIs. Anyway making a session for every request is a very bad idea.
    A session contains a connection pool inside. Connection reusage and keep-alive (both are on by default) may speed up total performance.
    A session context manager usage is not mandatory but await session.close() method should be called in this case.
    (https://docs.aiohttp.org/en/stable/client_quickstart.html)
    """
    await http_session.close()


if __name__ == '__main__':
    asyncio.run(main())
