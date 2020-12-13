""" Task 4: Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.

Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.

Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

from itertools import product


def get_all_pairs(indexs=None):
    pairs = []
    for i, j in product(indexs, indexs):
        if i == j:
            continue
        if (i, j) not in pairs and (j, i) not in pairs:
            pairs.append((i, j))

    print(pairs)


def count_equal_pairs(_list=None):


    get_all_pairs(idxs)

    #for i, j in product(idxs, idxs):
     #   print(i, j)


if __name__ == "__main__":
    input_list = '1 1 1'.split()
    count_equal_pairs(input_list)
