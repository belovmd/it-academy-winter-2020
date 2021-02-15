"""
    Task 6. Вводится число найти его максимальный делитель, являющийся
    степенью двойки. 10(2) 16(16), 12(4).
"""


def max_divider_pow2(n):
    """Нахождение максимального делителя от n, являющегося степенью двойки

    :param n: number
    :return: number. Число, которое является максимальный делителем степени
    двойки
    """
    pow2 = []
    max_divider = 0

    for i in range(1, n + 1):
        if i > n:
            break

        if (1 << i) <= n:
            pow2.append(1 << i)

        if not n % i and i in pow2:
            max_divider = i

    print(f"Максимальный делитель степени двойки для {n} - {max_divider}")
    return max_divider


max_divider_pow2(10)
