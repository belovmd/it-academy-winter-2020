""" Task 4: Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.

Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.

Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

from itertools import product


def get_all_pairs(indexes=None):
    """Получение всех пар индексов

    :param indexes:
    :return: список. Список сожержит кортежи вида: (i, j)
             где i, j - индексы элементов в списке
    """
    pairs = []
    for i, j in product(indexes, indexes):
        if i != j:
            if ((i, j) not in pairs) and ((j, i) not in pairs):
                pairs.append((i, j))

    return pairs


def count_equal_pairs(_list=None):
    """Подсчет пар элементов, равных друг другу

    :param _list: список чисел
    :return: число. Количество равных пар
    """
    pair_count = 0

    indexes = range(len(_list))
    pairs = get_all_pairs(indexes)

    for first_idx, second_idx in pairs:
        if _list[first_idx] != _list[second_idx]:
            continue
        pair_count += 1

    return pair_count


if __name__ == "__main__":
    input_list = '1 1 1 4'.split()

    # O(n**2) solution
    # print(count_equal_pairs(input_list))

    counter = {}
    for i in input_list:
        counter[i] = counter.get(i, 0) + 1

    pair_count = 0
    for value in counter.values():
        if value > 1:
            pair_count += (value * (value - 1)) // 2

    print(f"Количество пар равно {pair_count}")
