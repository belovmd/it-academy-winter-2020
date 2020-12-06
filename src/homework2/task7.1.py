""" Task 7.1:
Task name: No Idea!
Source: HackerRank
Level: Medium

There is an array of "n" integers. There are also 2 disjoint sets, "A"
and "B", each containing  integers.You like all the integers in set A and
dislike all the integers in set B. Your initial happiness is 0.
For each "i" integer in the array, if "i in A", you add 1 to your happiness.
If "i in B", you add -1 to your happiness. Otherwise, your happiness does
not change. Output your final happiness at the end.

Note: Since "A" and "B" are sets, they have no repeated elements.
However, the array might contain duplicate elements.
"""


def get_happiness(negative_set, positive_set, array=None):
    """Подсчет показателя "happiness" для списка

    :param negative_set: множество негативных элементов (дающих -1)
    :param positive_set: множество "позитивных" элементов (дающих +1)
    :param array: списко элементов
    :return: целое число. Показатель "happiness"
    """

    happiness = 0

    for neg, pos in zip(negative_set, positive_set):
        if pos in array:
            happiness += (1 * array.count(pos))
        if neg in array:
            happiness -= (1 * array.count(neg))

    return happiness


if __name__ == "__main__":

    input_list = [1, 3, 5, ]

    set_a = {3, 1, }  # множество позитивных элементов (дающих +1)
    set_b = {5, 7, }  # множество негативных элементов (дающих -1)

    if set_a.isdisjoint(set_b):
        print('happiness is ', get_happiness(set_b, set_a, input_list))
    else:
        print("Множества А и В имеют пересечения (общие элементы).")
