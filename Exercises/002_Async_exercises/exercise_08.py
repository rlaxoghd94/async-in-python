"""
Exercise 8

Write a Python program that uses asyncio queues to simulate a producer-consumer scenario with multiple producers and
a single consumer
"""
import asyncio
import random


class QueueMessageDTO:
    message_id: int
    message: str

    def __init__(self, message_id: int, message: str):
        self.message_id = message_id
        self.message = message if message else None


class Consumer:
    queue: asyncio.Queue[QueueMessageDTO]

    def __init__(self, queue: asyncio.Queue[QueueMessageDTO]):
        self.queue = queue

    async def consume(self):
        is_queue_empty = self.queue.empty()
        while not is_queue_empty:
            data = await self.queue.get()
            print(f'[consume] id: {data.message_id}, message: {data.message}')
            is_queue_empty = self.queue.empty()


class Producer:
    queue: asyncio.Queue[QueueMessageDTO]

    def __init__(self, queue: asyncio.Queue[QueueMessageDTO]):
        self.queue = queue

    async def produce(self, data: QueueMessageDTO):
        for i in range(0, 5):
            try:
                await self.queue.put(data)
            except asyncio.QueueFull:
                await asyncio.sleep(2)
                continue

            print(f'[produce] id: {data.message_id}, message: {data.message}')
            break  # queue put success


async def main():
    message_index: int = 0
    message_index_lock = asyncio.Lock()

    queue: asyncio.Queue[QueueMessageDTO] = asyncio.Queue()
    producers = [
        Producer(queue),
        Producer(queue),
        Producer(queue),
        Producer(queue),
        Producer(queue),
        Producer(queue),
    ]
    consumer = Consumer(queue)

    tasks = []

    # create producer tasks
    for producer in producers:
        random_tries = random.randint(1, 6)
        for i in range(0, random_tries):
            tasks.append(
                producer.produce(
                    QueueMessageDTO(message_index, f'message #{message_index}')
                )
            )

            async with message_index_lock:
                message_index += 1

    # create consumer task
    tasks.append(consumer.consume())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
