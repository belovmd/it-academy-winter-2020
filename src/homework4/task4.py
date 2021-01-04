"""
Даны два списка чисел.
Посчитайте, сколько различных чисел
входит только в один из этих списков.
"""

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = 0
result_list = list1 + list2
for element in list1:
    if list1.count(element) == result_list.count(element):
        result += 1
for element in list2:
    if list2.count(element) == result_list.count(element):
        result += 1
print(result)
