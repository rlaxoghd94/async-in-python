# Introduction

Introduction to asynchronous programming

In this document the followings will be covered:

- What a *synchronous programming* is
- What a *multithreading* is
- What an *asynchronous programming* is
- Why you might want to write an asynchronous program
- How to use python async features

---

## What is a *synchronous programming*?

| Synchronous programming is a programming model where operations take place sequentially - deepsource

In synchronous programming, operations occur one after the other in a sequential manner. The program will literally act
according to the lines of code written in files and execute the required "main flow" codes one-by-one.

This linear behaviour means that long-running operations are **blocking**, and the program will halt for the duration it
takes to complete each steps taken.

### How does synchronous programming work?

In synchronous programming, steps defined sequentially occur in the same order. So a program that invokes a synchronous
function `a()` and uses its outcome in a function `b()` would have to be written in the sequence where *a*, the primary
function, precedes *b*, the secondary function. This way, by the time the flow of control reaches the secondary
function, the outcome of the primary function will be available to the runtime.

```python
import time


def a() -> str:
    print('[a] starting...')

    time.sleep(2)
    print('[a] finished.\n')

    return 'a'


def b(param: str):
    print('[b] starting...')
    print(f'param: {param}')
    print('[b] finished.\n')


if __name__ == '__main__':
    a_val = a()
    b(a_val)
```

```commandline
[a] starting...
[a] finished.

[b] starting...
param: a
[b] finished.
```

In detail, `b()` cannot run until `a()` is finished as `a()` is blocking the whole program runtime.

---

## What is an *asynchronous programming*?

Asynchronous programming is a multithreaded model that's applied to networking and communications.

Asynchronous is a non-blocking architecture, which means it doesn't block further execution while one or more operations
are in progress. With async programming, multiple related operations can run concurrently without waiting for other
tasks to complete.

One way of programming asynchronous application is with low-code application development. Multiple developers can work
on projects simultaneously in a low-code platform, which helps accelerate the process of building apps.

Another example is texting, Texting is an asynchronous communication method. One person can text, and the recipient can
respond at leisure. In the meantime, the sender may do other things while waiting for a response.

```python
import asyncio


async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')


if __name__ == '__main__':
    asyncio.run(fn())

```

```commandline
This is 
asynchronous programming
and not multi-threading
```

Basically, asynchronous programming takes full advantages of cpu-bound and io-bound actions to be executed
simultaneously on a different thread. Opposed to synchronous programming, where every line of code will be executed
sequentially, asynchronous programming will `await` for a task to be finished on a different thread, while working on
different task at the same time.

### Async vs Sync

Async:

- is multi-thread(allows operations/programs to run in parallel)
- is non-blocking(will send multiple requests to a server)
- increases throughput because multiple operations can run at the same time

Sync:

- is single-thread(only one operation/program will run at a time)
- is blocking(will only send the server one request at a time and wait for that request to be answered by the server)
- is slower and more methodical

---

## Why you might want to write an asynchronous program

As mentioned above in "Async vs Sync", asynchronous program will take full advantage of the host machine performance
with better throughput and shorter processing time.

In production-wise settings, asynchronous programming will bring a large difference in the CCP(Cloud Computing Provider)
billing expenses when compared to a synchronous server.

---

## How to use python async features

use python native `asyncio` library

In order to use the async feature in python, you need to understand the concept of "Coroutine". Coroutine is a
concurrent task in asyncio programs. Python provides first-class coroutines and the asyncio module for running and using
them in python applications.

Coroutines are used to develop concurrent applications but are unlike thread-based and process-based concurrency
commonly used in python.

To be more specific, a coroutine is a function that can be suspended and resumed. It's often defined as a generalized
subroutine.

A subroutine can be executed, starting at one point and finishing at another point. whereas, a coroutine can be executed
then suspended, and resumed many times before finally terminating.

In sum, coroutines have control over when exactly they suspend their execution.

This may involve the use of a specific expression, such as an `await` expression in python, like a yield expression in a
python generator.

A coroutine may suspend for many reasons, such as executing another corouting, e.g. awaiting another task, or waiting
for some external resources, such as a socker connection or process to return data.

Coroutines are used for concurrency. My coroutines can be created and executed at the same time. They have control over
when they will suspend and resume, allowing them to cooperate as to when concurrent tasks are executed.

This is called *cooperative multitasking* and is different to the multitasking typically used with threads called
preemptive multitasking tasking.

Preemptive multitasking involves the operating system choosing what threads to suspend and resume when to do so, as
opposed to the tasks themselves deciding in the cas of cooperative multitasking.

### Coroutine vs Routine and Subroutine

A "routine" and "subroutine" often refer to the same thing in modern programming.

Perhaps more correctly, a routine is a program, whereas a subroutine is a function in the program.

A routine has subroutines.

It is a discrete module of expressions that is assigned a name, may take arguments and may return a value.

A subroutine is executed, runs through the expressions, and returns somehow. Typically, a subroutine is called by
another subroutine.

A coroutine is a generalization of a subroutine. This means that a subroutine is a special type of a coroutine.

A coroutine is like a subroutine in many ways, such as:

- They both are discrete named modules of expressions
- They both can take arguments, or not
- They both can return a value, or not

The main difference is that it chooses to suspend and resume its execution many times before returning and exiting.

### Coroutine vs Generator

A generator is a special function that can suspend its execution.

A generator function can be defined like a normal function although it uses a `yield` expression at the point it will
suspend its execution and return a value.

A generator function will return a generator iterator object that be traversed, such as via a for-loop. Each time the
generator is executed, it runs from the last point it was suspended to the next yield statement.

A coroutine can suspend or yield to another coroutine using an `await` expression. It will then resume from this point
once the awaited coroutine has been completed.

### Coroutine vs Task

A subroutine and a coroutine may represent a "task" in a program.

However, in Python, there is a specific object called an `asyncio.Task` object.

A coroutine can be wrapped in an asyncio.Task object and executed independently, as opposed to being executed directly
within a coroutine. The Task object provides a handle on the asynchronously execute coroutine.

| Task is a wrapped coroutine that can be executed independently

This allows the wrapped coroutine to execute in the background. The calling coroutine can continue executing
instructions rather than awaiting another coroutine.

A Task cannot exists on its own, it must wrap a coroutine.

### Coroutine vs Thread

A coroutine is more lightweight than a thread.

A coroutine is defined as a function, whereas a thread is an object created and managed by the underlying operating
system and represented in Python as a `threading.Thread` object.

This means that coroutines are typically faster to create and start executing and take up less memory. Conversely,
threads are slower than coroutines to create and start and take up more memory.

Coroutines execute within one thread, therefore a single thread may execute many coroutines.

### Coroutine vs Process

A coroutine is more lightweight than a process(thread is as well).

A process is a computer program. It may have one or many threads.

A Python process is in fact a separate instance of the Python interpreter.

Processes, like threads, are created and managed by the underlying operating system and are represented by
a `multiprocessing.Process` object.

This means that coroutines are significantly faster than a process to create and start and take up much less memory.

A coroutine is just a special function, whereas a Process is an instance of the interpreter that has at least one
thread.

## How to use a coroutine in python

Python provides coroutines for concurrency in two main ways:

1. through specific addition to the language, e.g. `async` and `await` expressions
2. through a specific module in the standard library. e.g. `asyncio` module

In production setting-wise speaking, although coroutine is a single process, single threaded architecture, it enables
concurrency for the application(it wouldn't enable parallelism as no additional processes are being spawned). Therefore,
it'd be wise to control the size of concurrency occurring within the application execution. The most common method is to
create a pool of semaphores so the coroutines can hold on to the execution within the desired concurrency limit. This
would mean that you would need to create a queue of some sort of coroutines waiting for execution so that the
application can seamlessly schedule the coroutine execution as you desire.

### How to define a Coroutine

A coroutine can be defined via the `async def` expression.

```python
import asyncio


async def custom_coro():
    ...
```

A coroutine defined with the `async def` expression is referred to as a "coroutine function".

A coroutine can then use coroutine-specific expressions within it, such as `await`, `async for`, and `async with`.

```python
import asyncio


async def custom_coro():
    await asyncio.sleep(1)
```

### How to create a coroutine

Once a coroutine is defined, it can be created.

```python
# create a coroutine
coro = custom_coro()
```

This does not execute the coroutine, but it returns a "coroutine" object.

A "coroutine" Python object has methods, such as `send()` and `close()`. It is a type.

- generators(including coroutines) are essentially function that can yield values multiple times, and you can't simply
  just pass on a param as an input; rather, you have to pass the param value using the `.send()` extension function.
    - when you call a `send()` on a generator(including coroutine), the subroutine receives the data passed on and
      continues execution until it hits a `yield` statement within the subroutine, at which point it yields the value
      back to the caller

A coroutine object is an awaitable if you check the type.

### How to run a coroutine from Python

Coroutines can be defined and created, but they can only be executed within an event loop.

The event loop that executes coroutines, manges the cooperative multitasking between coroutines.

The typical way to start a coroutine event loop is via the `asyncio.run()` function.

This function takes one coroutine and returns the value of the coroutine. The provided coroutine can be used as the
entry point into the coroutine-based program.

```python
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

```

---

## References

- python async features - [realpython](https://realpython.com/python-async-features/)
- synchronous
  programming - [deepsource](https://deepsource.com/glossary/synchronous-programming#:~:text=Synchronous%20programming%20is%20a%20programming,and%20has%20returned%20an%20outcome.)
- asynchronous vs synchronous
  programming - [mendix](https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/)
- what is a coroutine in python - [superfastpython](https://superfastpython.com/python-coroutine/)
- ThreadPoolExecutor vs Asyncio in
  Python - [superfastpython](https://superfastpython.com/threadpoolexecutor-vs-asyncio/)
- Python 비동기 프로그래밍 제대로 이해하기(1/2) - [humminglab](https://blog.humminglab.io/posts/python-coroutine-programming-1/)
- Python 비동기 프로그래밍 제대로 이해하기(2/2) - [humminglab](https://blog.humminglab.io/posts/python-coroutine-programming-2/)
