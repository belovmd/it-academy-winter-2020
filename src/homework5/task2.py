"""Создайте декоратор, который хранит результаты вызовов функции
    (за все время вызовов, не только текущий запуск программы)
"""


from datetime import datetime


def my_dec(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        func_start = datetime.now()
        result = func(*args, **kwargs)
        with open('task2.txt', 'a') as results:
            results.writelines('{}, {}, {}'.format(func_name, func_start,
                                                   result))

        return result

    return wrapper


@my_dec
def my_func(a, b):
    """Count the sum of elements.

    :param a: an integer.
    :param b: an integer.
    :return: an integer, the sum of element.
    """
    return a + b


print(my_func(2, 3))
