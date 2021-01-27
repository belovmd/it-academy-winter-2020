"""Создайте декоратор, который хранит результаты вызовов функции
    (за все время вызовов, не только текущий запуск программы)
"""


from datetime import datetime
from datetime import timedelta


def my_dec(func):
    all_results = {}
    func_name = func.__name__
    call_counter = 0

    def wrapper(*args, **kwargs):
        nonlocal all_results, func_name, call_counter

        call_counter += 1
        (all_results.setdefault(call_counter, [func_name])
         .append(func(*args, **kwargs)))

        print(all_results)
        return func(*args, **kwargs)

    return wrapper


@my_dec
def my_func(a, b):
    """Count the sum of elements.

    :param a: an integer.
    :param b: an integer.
    :return: an integer, the sum of element.
    """
    return a + b


start = datetime.now()
cache_lifetime = timedelta(days=30)
func_expiration = start + cache_lifetime

if datetime.now() <= func_expiration:
    my_func(3, 5)
