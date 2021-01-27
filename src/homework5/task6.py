"""Бинарные операции
   Вводится число найти его максимальный делитель, являющийся степенью двойки.
   10(2) 16(16), 12(4).
   Задачу поместите в файл task6.py в папке src/homework5.
"""


def max_divider(number):
    divider = 1
    counter = 0
    while True:
        power_number = 2 << counter
        if power_number > number:
            return divider
        elif not number % power_number:
            divider = power_number
            counter += 1
        else:
            counter += 1


if __name__ == "__main__":
    n = int(input())
    print(max_divider(n))
