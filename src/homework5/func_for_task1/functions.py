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
