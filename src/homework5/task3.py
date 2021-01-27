"""Реализовать функцию get_ranges которая получает на вход непустой список
   неповторяющихся целых чисел, отсортированных по возрастанию,
   которая этот список “сворачивает”
   get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
   get_ranges([4,7,10]) // "4,7,10"
   get_ranges([2, 3, 8, 9]) // "2-3,8-9"
   Задачу поместите в файл task3.py в папке src/homework5.
"""


def get_ranges(not_empty_list):
    collapsed_lst_in_str = ''

    for index, el in enumerate(not_empty_list[:-1]):
        if el + 1 != not_empty_list[index + 1]:
            collapsed_lst_in_str += f'{el},'

        elif el + 1 == not_empty_list[index + 1] and el - 1 != not_empty_list[index - 1]:
            collapsed_lst_in_str += f'{el}-'

    collapsed_lst_in_str += f'{not_empty_list[-1]}'
    print(collapsed_lst_in_str)


lst_ = [1, 2, 3, 4, 8, 9, 10]
get_ranges(lst_)
