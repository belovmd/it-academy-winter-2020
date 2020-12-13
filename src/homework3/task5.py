""" Task 5: Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только
один раз. Элементы нужно выводить в том порядке, в котором они встречаются
в списке.
"""


def print_unique_elements(_list=None):
    """

    :param _list:
    :return:
    """
    count_dict = {}

    for element in _list:
        count_dict[element] = count_dict.get(element, 0) + 1

    for key, value in count_dict.items():
        if value == 1:
            print(key)


if __name__ == "__main__":
    _list = [1, 2, 2, 3, 4, 4, 4, 4, 5, 7, 'py', 'hello', 'hello', ]
    print_unique_elements(_list)
