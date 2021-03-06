""" Создайте декоратор, который вызывает задекорированную функцию пока она
    не выполнится без исключений (но не более n раз - параметр декоратора).
    Если превышено количество попыток, должно быть возбуждено исключение
    типа TooManyErrors
"""
import functools
import random


def runner(tries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n == tries:
                        raise IOError("TooManyErrors")
        return wrapper
    return decorator


@runner(tries=10)
def do():
    if random.randint(0, 10) > 1:
        print('ok')
    else:
        return "not ok"


do()
