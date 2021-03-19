"""Написать программу которая находит ближайшую степень
   двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def degree(a):
    i = 0
    while True:
        b = abs(a - (1 << i))
        c = abs(a - (1 << i + 1))
        if c > b:
            break
        else:
            i += 1
    return 1 << i


print(degree(10))
print(degree(20))
print(degree(1))
print(degree(13))


"""
def degree(a):
    i = 0
    while 2 ** i <= a:
        i += 1
    b = (2 ** (i - 1))
    c = (2 ** i)
    if a - b < c - a:
        return b
    else:
        return c


a = int(input('Введите целое четное число: '))
print(degree(a))
"""
