'''
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
'''


def max_divider(number):

    result = 1

    for _ in range(number):
        variable = 1 << _

        if not number % variable:
            result = variable
        if variable >= number:
            return result


print(max_divider(12))
