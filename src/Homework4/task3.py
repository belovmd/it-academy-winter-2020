'''
Даны два списка чисел. Посчитайте,
сколько различных чисел содержится одновременно
как в первом списке, так и во втором.
'''


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 7, 3, 8, 5, 9]
result = set(list_1) & set(list_2)
print(list(result))
print('различных чисел - ' + str(len(result)))
