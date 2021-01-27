"""Реализовать функцию get_ranges которая получает на вход непустой
    список неповторяющихся целых чисел, отсортированных по возрастанию,
    которая этот список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    """Collapse a list.

    :param lst: a list of unique integers sorted in ascending order.
    :return: a string, a collapsed list. Form: "0-4,7-8,10".
    """
    collapsed_lst = ''
    for num in range(len(lst) - 1):
        if lst[num] + 1 == lst[num + 1] and lst[num] - 1 != lst[num - 1]:
            collapsed_lst += str(num) + '-'
        elif lst[num] + 1 != lst[num + 1]:
            collapsed_lst += str(num) + ','
    collapsed_lst += str(lst[-1])
    print(collapsed_lst)


if __name__ == '__main__':
    lst = [0, 1, 2, 3, 4, 7, 8, 10]
    get_ranges(lst)
