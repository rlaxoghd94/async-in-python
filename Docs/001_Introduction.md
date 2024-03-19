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

## References

- [realpython](https://realpython.com/python-async-features/)
- [deepsource](https://deepsource.com/glossary/synchronous-programming#:~:text=Synchronous%20programming%20is%20a%20programming,and%20has%20returned%20an%20outcome.)