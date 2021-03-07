'''
Реализовать функцию get_ranges которая получает на вход непустой
список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''


def get_ranges(list_):
    result = ''
    for var, el in enumerate(list_[:-1]):
        if el + 1 != list_[var + 1]:
            result += f'{el},'
        elif el + 1 == list_[var + 1] and el - 1 != list_[var - 1]:
            result += f'{el}-'
    result += f'{list_[-1]}'
    print(result)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
