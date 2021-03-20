"""Написать программу которая находит ближайшую степень двойки к введенному
    числу. 10(8), 20(16), 1(1), 13(16)
"""


def power_of_two(n):
    """Finds the closest power of two to the input number.

    :return: int, the closest power.
    """

    primary_power = 1
    while n >> primary_power:
        primary_power += 1
    if abs((1 << primary_power) - n) > abs((n - (1 << (primary_power - 1)))):
        return 1 << (primary_power - 1)
    else:
        return 1 << primary_power


if __name__ == '__main__':
    num = int(input())
    print(power_of_two(num))
