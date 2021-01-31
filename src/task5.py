"""
    Task 5. Написать программу которая находит ближайшую степень двойки
    к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def nearest_pow2(n):
    """ Нахождение ближайшей степени двойки к n

    :param n: number.
    :return: number. Число, которое является ближайшей степенью двойки к n
    """
    current, prev = 0, 0

    for i in range(n):
        current = n - (1 << i)

        if current > 0:
            prev = current
        else:
            nearest = n + -current if -current < prev else n - prev
            print(f"Ближайшая степень двойки для {n} - ", nearest)
            return nearest


nearest_pow2(10)
