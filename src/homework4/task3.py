"""
Даны два списка чисел.
Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""

list1 = [1, 2, 3, 4, 5, 8, 2]
list2 = [4, 5, 6, 7, 8]
result = 0
result_list = list1 + list2
for element in list1:
    if list1.count(element) < result_list.count(element):
        result += 1
print(result)
