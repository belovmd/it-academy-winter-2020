""" Task 3:
Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""

if __name__ == "__main__":
    _list1 = [1, 2, 3, 4, 5, 5, 6, 7, ]
    _list2 = [5, 6, 6, 7, 7, 7, 8, 9, 10, ]

    number_of_different = len(set(set(_list1) & set(_list2)))

    print(f"Count = {number_of_different}")
