from fractions import Fraction

"""Проект Эйлера. https://euler.jakumo.org/problems/pg/1.html.
   Обобщите указанную задачу на свое усмотрение, решите ее,
   покройте тестами.
"""

"""Рассмотрим дробь n/d, где n и d являются положительными
   целыми числами. Если n<d и НОД(n,d) = 1, то речь идет о
   сокращенной правильной дроби.
   Если перечислить множество сокращенных правильных дробей
   для d ≤ 8 в порядке возрастания их значений, получим:
   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7,
   3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
   Нетрудно заметить, что дробь 2/5 расположена непосредственно
   слева от дроби 3/7.
   Перечислив множество сокращенных правильных дробей для d ≤ 10**6
   в порядке возрастания их значений, найдите числитель дроби,
   расположенной непосредственно слева от дроби 3/7.
"""


def numerator(c):
    # Создаем множество дробей,чтобы убрать повторы и сократить дроби
    # убираем дроби, где числитель больше знаменателя либо ему равен
    set_fraction = {Fraction(n, d) for d in range(2, c + 1)
                    for n in range(1, c) if n < d and n != d}
    # преобразуем в список, чтобы отсортировать по возрастанию
    list_fraction = list(set_fraction)
    list_fraction.sort()
    # Находим нужный элемент
    for elem in range(len(list_fraction)):
        if list_fraction[elem] == Fraction(3, 7):
            required_element = list_fraction[elem - 1]
            # Выводим искомый числитель
            return required_element
