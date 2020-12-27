"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""

for element in range(1, 101):
    if not element % 5 and not element % 3:
        print('FizzBuzz', end=', ')
    elif not element % 5:
        print('Buzz', end=', ')
    elif not element % 3:
        print('Fizz', end=', ')
    else:
        print(element, end=', ')
