""" Создайте декоратор, который хранит результаты вызовов функции
    (за все время вызовов, не только текущий запуск программы)
"""

import functools
import time


def dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Номер вызова функции - {wrapper.calls}")
        end = time.perf_counter()
        run = (time.perf_counter() - end)
        print(f"Функция выполнена за - {run} sec")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@dec
def funck(x, y):
    time.sleep(3)
    return x + y


print(funck(1, 2))
print(funck(3, 4))
