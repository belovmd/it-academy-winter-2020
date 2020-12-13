""" Task 1: FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""


def fizzbuzz():
    """

    :return: None
    """
    for number in range(1, 101):
        if (not number % 3) and (not number % 5):
            print('FizzBuzz')
            continue
        if not number % 3:
            print('Fizz')
            continue
        if not number % 5:
            print('Buzz')
            continue


if __name__ == '__main__':
    fizzbuzz()