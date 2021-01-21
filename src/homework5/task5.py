""" Task 5: Ближайшая степень двойки
Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def nearest_power_of_2(number):
    """Поиск ближайшеего числа равного степени двойки

    :param number: входное число
    :return: число. Является степенью двойки
    """
    prev_power = 1

    for i in range(number):
        curr_power = 1 << i

        if curr_power >= number:
            if curr_power - number < number - prev_power:
                return curr_power
            else:
                return prev_power

        prev_power = curr_power


if __name__ == "__main__":
    n = 13

    print(nearest_power_of_2(n))
