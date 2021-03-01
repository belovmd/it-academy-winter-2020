# Реализовать функцию get_ranges которая получает
# на вход непустой список неповторяющихся целых
# чисел, отсортированных по возрастанию, которая
# этот список “сворачивает”
# def get_ranges(self):
import copy
import re

def get_ranges(list_num):
    list_all = []
    list_part = []
    result_str = ''

    for index in range(len(list_num) + 1):
        if index < len(list_num):

            if list_num[index] == list_num[len(list_num) - 1]:
                list_part.append(list_num[index])
                list_all.append(copy.copy(list_part))

            elif list_num[index] + 1 == list_num[index + 1]:
                list_part.append(list_num[index])

            else:
                list_part.append(list_num[index])
                list_all.append(copy.copy(list_part))
                list_part.clear()

    for el in list_all:
        if len(el) >= 2:
            result_str += f' {el[0]}-{el[-1]} '
        else:
            result_str += f' {str(*el)} '

    result_str = result_str.replace('  ', ', ')

    return print(f'Свернули: "{result_str}"')


# get_ranges([1, 2, 3, 5, 6, 7, 8, 90, 91, 92, 100])
get_ranges([1, 2, 4, 5, 8, 20])
