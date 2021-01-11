"""Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный
5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


for element in range(1, 101):
    if element % 15 == 0:
        print('FIZZBUZZ')
    elif element % 5 == 0:
        print('BUZZ')
    elif element % 3 == 0:
        print('FIZZ')
    else:
        print(element)
