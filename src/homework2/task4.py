""" Task 4:
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""


def count(string):
    """Подсчёт строчных и прописных букв

    :param string: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """
    lower_count = 0
    for char in string:
        if char.lower() == char:
            lower_count += 1

    return lower_count, len(string) - lower_count


print(count("A"))