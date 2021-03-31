import math

"""
Оформите указанную задачу из прошлых домашних в виде функции и
покройте тестами. Учтите, что в функцию могут быть переданы некорректные
значения, здесь может пригодится ‘assertRaises’. Не нужно переделывать
функцию для того чтобы она ловила все возможные ситуации сама.
Вариант 15
Домашняя 4.
Задача 5.
Задача 74
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def func(element):
    dct = {}

    for element in element.split():
        dct[element] = dct.get(element, 0) + 1
    for values_ in dct.values():
        if values_ > 1:
            result = (math.factorial(values_) // (math.factorial(values_ - 2) * 2))

            print(result)
            return element


func('1 1 1 1')
