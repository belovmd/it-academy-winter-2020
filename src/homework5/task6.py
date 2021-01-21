""" Task 5: Ближайшая степень двойки
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_divisor(number):
    """ Поиск максимального делителя являющегося степенью двойки

    :param number: число
    :return: число. Максимальный делитель являющейся степенью двойки
    """
    prev_power = 1

    for i in range(number):
        curr_power = 1 << i

        if not number % curr_power:
            prev_power = curr_power
        if curr_power >= number:
            return prev_power


if __name__ == "__main__":
    n = 10
    print(max_divisor(n))
