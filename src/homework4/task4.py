"""
Даны два списка чисел.
Посчитайте, сколько различных чисел входит
только в один из этих списков
"""
lst_1 = [1, 2, 3, 6, 8]
lst_2 = [3, 4, 5, 7, 8]
result = set(lst_1) ^ set(lst_2)
print(len(result))
