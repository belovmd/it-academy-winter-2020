"""
Task 7.2:
Task name: Number of Good Pairs
Source: LeetCode
Level: Easy

Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
"""

from itertools import product


def get_good_pairs(numbers):
    """
    Получение всех пар индексов, удовлетворяющих условию "хорошей пары"

    :param numbers: список чисел
    :return: список. Список содержит кортежи вида: (i, j) - "хорошая пара",
        где i,j индексы элементов во входном списке numbers
    """
    pairs = []

    ids = range(len(numbers))  # все индексы списка nums ( 0...len(nums) - 1 )

    for first_idx, second_idx in product(ids, ids):  # избавляемся от вложенных циклов
        if first_idx >= second_idx:
            continue
        if numbers[first_idx] == numbers[second_idx]:
            pairs.append((first_idx, second_idx))

    return pairs


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3, ]
    print(get_good_pairs(nums))


