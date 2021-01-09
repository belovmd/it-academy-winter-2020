"""
4. Пары элементов
Дан список чисел.
Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу,
образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

numbers = '1 1 2 2 67 67 1 1 2'
print(numbers)
list1 = numbers.split()
pairs = 0
numbers_amount = {element: list1.count(element) for element in list1}
for key in numbers_amount:
    n = 0
    while n < numbers_amount[key] - 1:
        n += 1
        pairs += n
print(pairs)
