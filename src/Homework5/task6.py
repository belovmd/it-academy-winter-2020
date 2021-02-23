"""Вводится число. Найти его максимальный делитель,
   являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_div(a):
    i = 1
    div = 1
    while True:
        div = div << 1
        if a % div != 0:
            break
        i = div
    return i


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
