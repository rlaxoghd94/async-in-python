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
