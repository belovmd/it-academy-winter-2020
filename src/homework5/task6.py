""" Вводится число найти его максимальный делитель,
    являющийся степенью двойки. 10(2) 16(16), 12(4)
"""


def max_divider(number):

    result = 1

    for i in range(number):
        variable = 1 << i

        if not number % variable:
            result = variable
        if variable >= number:
            return result


if __name__ == "__main__":

    digit = int(input())
    print(max_divider(digit))
