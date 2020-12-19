'''
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами. 
Выходные данные - количество пар. 
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''
import math

lst = '1 1 1 1 2 2 2 3 3 3 4 4 4 5'
dct = {}

for element in lst.split():
    dct[element] = dct.get(element, 0) + 1

for value in dct.values():
    if value > 1:
        value = (math.factorial(value) // (math.factorial(value - 2) * 2))
        # по формуле C == n! // (n - k)! * k!, где n - кол-во объектов,
        # k - пара объектов, C - кол-во комбинаций.
        print(value)


#РЕШЕНИЕ2##########################
from itertools import combinations as cmb
print(sum(1 for x in cmb(map(int, input().split()), 2) if x[0]==x[1]))
###########################
a = x.split() # например 1 1 1 1 1
print(sum(a.count(x) - 1 for x in a) // 2