import functools
import random
import time


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.number += 1
        print(f"{wrapper.number} вызов {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper.number = 0
    return wrapper


def timer(func):
    def function(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"время вызова {run_time:.8f} sec")
        return value
    return function


@count_calls
@timer
def add(a, b):
    print(f'random {random.randint(a, b)}')
    return a + b


add(0, 10)
print()
add(10, 20)
print()
add(20, 30)
