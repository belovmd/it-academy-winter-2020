from functools import wraps
from datetime import datetime


"""
    Task 2. Создайте декоратор, который хранит результаты вызовов функции
    (за все время вызовов, не только текущий запуск программы)
"""


def logger(func):
    """Сохранение результатов работы функции в файл

    :param func: function. Функция, результаты которой будут сохраняться в
    файле
    :return: function. Обертка над func, которая будет возвращать результат
    работы функции func
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None

        try:
            result = func(*args, *kwargs)
        except Exception as err:
            result = f"Error: {err}"
        finally:
            date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            func_name = func.__name__

            with open('log.txt', 'a') as file:
                file.write(f"{date_time} - {func_name} - {result}\n")

        print(f"log result - {result}")
        return result
    return wrapper


@logger
def cubes(n):
    """Возведение числа в степень 3

    :param n: number.
    :return:  number. Число n возведенное в степень 3
    """
    return n ** 3


cubes(3)
