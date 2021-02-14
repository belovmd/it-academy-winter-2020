"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""

import datetime
from os import path
import pytz


if path.exists('functions_results.txt'):
    pass
else:
    f = open('functions_results.txt', 'w')
    f.close()


def decorator(func):
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        with open('functions_results.txt', 'a') as ff:
            ff.write('Date: {date}, Function: {name}, '
                     'Result: {result} \n'.
                     format(name=func.__name__,
                            date=datetime.datetime.now(pytz.UTC).strftime(
                                '%Y-%m-%d %H:%M:%S %Z %z'),
                            result=func_result))
        return func_result
    return wrapper


@decorator
def my_f(a):
    return a


my_f(5)
