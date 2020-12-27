""" Task 1: FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""


def fizzbuzz(number):
    """ Решение задачи FizzBuzz

    :param number: число
    :return: string. Строка возвращается в зависимости от
        кратности числа
    """
    if not number % 15:
        return 'FizzBuzz'
    if not number % 3:
        return 'Fizz'
    if not number % 5:
        return 'Buzz'

    return number


if __name__ == '__main__':
    for number in range(1, 101):
        print(fizzbuzz(number))
