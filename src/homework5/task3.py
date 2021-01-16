""" Task 3:
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая
этот список “сворачивает”:
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""

from functools import reduce


def tmp(s1, s2):
    return


def get_ranges(lst=None):
    flag = False
    result = ''
    for idx, elem in enumerate(lst[:]):
        if abs(elem - lst[idx - 1]) > 1:
            result += f"- {lst[idx + 1]},{elem}"
            flag = True
        if flag:
            result += str(elem) + '-'
            flag = False
        else:
            continue


    print(result)

    return None


if __name__ == "__main__":
    input_list = [0, 1, 2, 3, 4, 7, 8, 10]
    print(get_ranges(input_list))
