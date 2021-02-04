"""Написать программу которая находит ближайшую степень двойки к введенному
    числу. 10(8), 20(16), 1(1), 13(16)
"""


def power_of_two(n):
    """ Finds the closest power of two to the input number.

    :return: int, the closest power.
    """

    primary_power = 1
    while 2 ** primary_power < n:
        primary_power += 1
    if (2 ** primary_power - n) > (n - (2 ** (primary_power - 1))):
        return 2 ** (primary_power - 1)
    else:
        return 2 ** primary_power


if __name__ == '__main__':
    num = int(input())
    print(power_of_two(num))
