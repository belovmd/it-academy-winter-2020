"""Создайте декоратор, который хранит результаты вызовов функции
   (за все время вызовов, не только текущий запуск программы)
   Задачу поместите в файл task2.py в папке src/homework5.
"""


import logging
import functools
import time


def count_calls(func):
    @functools.wraps(func)
    def wrapper_c(*args, **kwargs):
        wrapper_c.num_calls += 1
        print(f"{wrapper_c.num_calls} вызов функции {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper_c.num_calls = 0
    return wrapper_c


def logger(func):
    log = logging.getLogger(__name__)

    def wrapper(a, b):
        log.info("Вызов функции ", func.__name__)
        ret = func(a, b)
        log.info("Вызвана функция ", func.__name__)
        return ret

    return wrapper


def timer(func):
    def function(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Функция выполнена за {run_time:.8f} sec")
        return value

    return function


@logger
@count_calls
@timer
def add(a, b):
    print('a + b =', a + b)
    return a + b


add(10, 20)
print()
add(20, 30)
print()
add(30, 40)
