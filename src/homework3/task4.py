"""
    Task 4. Пары элементов

    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
    другу. Считается, что любые два элемента, равные друг другу образуют одну
    пару, которую необходимо посчитать.

    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

sting_of_numbers = "5 5 8 8 8 1 4"
counting_numbers = {}
pairs = {}

count = 0
counted_elms = set()

for num in sting_of_numbers.split():
    counting_numbers[num] = counting_numbers.get(num, 0) + 1

    if counting_numbers[num] > 1:
        if num in counted_elms:
            count -= pairs[num]

        pairs[num] = pairs.get(num, 0) + (counting_numbers[num] - 1)

        count += pairs[num]
        if num not in counted_elms:
            counted_elms.add(num)

print(count)
