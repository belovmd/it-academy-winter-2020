""" Task 3:
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая
этот список “сворачивает”:
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst=None):
    """Свёртка списка

    :param lst: cписок.
    :return: строка.
    """
    range_string = ''

    for idx, elem in enumerate(lst[:-1]):
        if elem + 1 != lst[idx + 1]:
            range_string += f'{elem},'
        elif elem + 1 == lst[idx + 1] and elem - 1 != lst[idx - 1]:
            range_string += f'{elem}-'
    range_string += f'{lst[-1]}'

    return range_string


if __name__ == "__main__":
    input_list = [2, 3, 8, 9]
    print(get_ranges(input_list))
