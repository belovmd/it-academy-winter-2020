'''
Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
'''


def binary_operators(number):

    result = 1

    for _ in range(number):
        var = 1 << _

        if var >= number:
            if var - number < number - result:
                return var
            else:
                return result

        result = var


print(binary_operators(10))
