"""	Реализовать функцию get_ranges которая получает на вход непустой список
    неповторяющихся целых чисел, отсортированных по возрастанию,
    которая этот список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    ([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(num_list):

    ranges = ""
    last_num = len(num_list) - 1

    for var, element in enumerate(num_list):
        next_num = num_list[var + 1] if var != last_num else None

        if not ranges or ranges[-1] == ",":
            ranges += str(element)
        elif (next_num is None) or (next_num != element + 1):
            ranges += f"-{element}"

        if (next_num is not None) and (next_num != element + 1):
            ranges += ','

    print(ranges)
    return ranges


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
get_ranges([])
