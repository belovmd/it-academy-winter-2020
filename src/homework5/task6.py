"""Вводится число найти его максимальный делитель, являющийся степенью двойки.
    10(2) 16(16), 12(4).
"""


def max_divider(n):
    """ Finds the number's maximum divider, which is a power of two.

    :return: int, the maximum divider.
    """
    primary_power = 0
    while not n % (2 ** primary_power):
        primary_power += 1
    return 2 ** (primary_power - 1)


if __name__ == '__main__':
    num = int(input())
    print(max_divider(num))
