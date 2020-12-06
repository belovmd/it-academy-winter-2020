""" Task 3:
Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


def get_unique_substring(string):
    """Конструирование подстроки.

    :param string: входная строка
    :return: строка. Строка содержит только уникальные
        символы.
    """

    unique_chars = []

    string = string.replace(" ", "")

    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)

    return "".join(unique_chars)


if __name__ == "__main__":
    input_string = 'abc cde def'
    print(get_unique_substring(input_string))
