""" Дан список чисел. Посчитайте, сколько в нем пар элементов,
   равных друг другу. Считается, что любые два элемента, равные друг другу
   образуют одну пару, которую необходимо посчитать.
   Входные данные - строка из чисел, разделенная пробелами.
   Выходные данные - количество пар.
   Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.
"""

string_num = '1 1 2 2 3 3 3 4 4 4 4'
lst = string_num.split()
pairs = 0

numbers = {element: string_num.count(element) for element in lst}
for key in numbers:
    num = 0
    while num < numbers[key] - 1:
        num += 1
        pairs += num
print(pairs)
