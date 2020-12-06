""" Task 4:
Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.
"""


def count(string):
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


print(count("DBCРебус!!!dfgERT"))
