"""	Реализовать функцию get_ranges которая получает на вход непустой список
    неповторяющихся целых чисел, отсортированных по возрастанию,
    которая этот список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    ([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(num_list):

    lst_instr = ''

    for var, element in enumerate(num_list[:-1]):
        if element + 1 != num_list[var + 1]:
            lst_instr += f'{element},'

        elif element + 1 == num_list[var + 1] \
                and element - 1 != num_list[var - 1]:
            lst_instr += f'{element}-'

    lst_instr += f'{num_list[-1]}'
    print(lst_instr)


notempty_list = [1, 2, 3, 4, 8, 9, 10]
get_ranges(notempty_list)
