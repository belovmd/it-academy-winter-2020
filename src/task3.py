"""
    Task 3. Реализовать функцию get_ranges которая получает на вход непустой
    список неповторяющихся целых чисел, отсортированных по возрастанию,
    которая этот список “сворачивает”

    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(num_list):
    """Сворачивание элеменов из списка num_list в строку

    :param num_list: list[int]. Непустой список неповторяющихся целых чисел
    :return: string. Свернутый список чисел представленный строкой
    """
    ranges = ""

    for i, num in enumerate(num_list):
        if i == len(num_list) - 1:
            if ranges[-1] != ",":
                ranges += f"-{num}"
            else:
                ranges += str(num)
            break

        if not ranges or ranges[-1] == ",":
            if num_list[i + 1] == num + 1:
                ranges += str(num)
            else:
                ranges += f"{num},"
            continue

        if num_list[i + 1] == num + 1:
            continue
        else:
            ranges += f"-{num},"

    print(ranges)
    return ranges


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
