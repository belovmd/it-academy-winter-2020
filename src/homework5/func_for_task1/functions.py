"""
Функции для импорта
"""


def count(string='AbAb'):
    """Подсчёт строчных и прописных букв
    :param string: входная строка
    :return: кортеж. Первый элемент - число строчных букв, второй элемент -
        число прописных букв
    """

    lower_count, upper_count = 0, 0

    for char in string:
        if 'a' <= char <= 'z':
            lower_count += 1
        if 'A' <= char <= 'Z':
            upper_count += 1

    return lower_count, upper_count


def fibonacci(n=10):
    """Вычисление n-го числа Фибоначчи
    :param n: номер числа
    :return: число. Возвращает n-е число Фибоначчи
    """

    n1, n2 = 1, 1
    for _ in range(n - 2):
        n1, n2 = n2, n2 + n1

    return n2


def print_unique_elements(_list=[1, 2, 2, 3, 4, 4, ]):
    """Нахождение и вывод в консоль уникальных элементов списка

    :param _list: список элементов
    :return: None
    """

    count_dict = {}

    for element in _list:
        count_dict[element] = count_dict.get(element, 0) + 1

    unique_elem = list()

    for key, value in count_dict.items():
        if value == 1:
            unique_elem.append(key)

    return unique_elem
