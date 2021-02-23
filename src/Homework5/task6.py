"""Вводится число. Найти его максимальный делитель,
   являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_div(a):
    i = 0
    while (a << 1) != 0:
        i += 1
        a = (a << 1)
    return 2 ** i

a = int(input('Введите целое четное число: '))
print(max_div(a))


"""
def max_div(a):
    i = 0
    while a % 2 == 0:
        i += 1
        a = a // 2
    return 2 ** i


a = int(input('Введите целое четное число: '))
print(max_div(a))
"""