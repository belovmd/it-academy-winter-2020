"""Даны два списка чисел. Посчитайте,
 сколько различных чисел входит только
 в один из этих списков
"""


lst_1 = [1, 8, 6, 4, 2, 8]
lst_2 = [1, 8, 12, 3, 18, 4]

set_ = set(lst_1) ^ set(lst_2)
print("Числа, которые входят только в один список", set_)
print("Количество  чисел, которые входят только в один список", len(set_))
