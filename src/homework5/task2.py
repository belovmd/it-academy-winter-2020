""" Создайте декоратор, который хранит результаты вызовов функции
    (за все время вызовов, не только текущий запуск программы)
"""

from datetime import datetime
import time


def dec(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        result = func(*args, **kwargs)
        file = open("task2_results.txt", "a")
        file.write(f"{name} : {date_time} - result: {result}\n")
        return result
    return wrapper


@dec
def func_test(x, y):
    time.sleep(3)
    return x + y


print(func_test(1, 2))
print(func_test(5, 7))
