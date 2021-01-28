"""Реализовать функцию get_ranges которая получает на вход
 непустой список неповторяющихся целых чисел, отсортированных
  по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(_list):
    var_ranges = ''

    for value, el in enumerate(_list[:-1]):
        if el + 1 != _list[value + 1]:
            var_ranges += f'{el},'

        elif el + 1 == _list[value + 1]\
                and el - 1 != _list[value - 1]:
            var_ranges += f'{el}-'

    var_ranges += f'{_list[-1]}'
    print(var_ranges)


to_check = [1, 2, 3, 4, 8, 9, 10]
get_ranges(to_check)
