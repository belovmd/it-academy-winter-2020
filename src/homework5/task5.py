""" Написать программу которая находит ближайшую степень двойки
    к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def number_close(number):

    result = 1

    for i in range(number):
        variable = 1 << i

        if variable >= number:
            if variable - number < number - result:
                return variable
            else:
                return result

        result = variable


if __name__ == "__main__":

    digit = int(input())
    print(number_close(digit))
