"""
1. FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратны 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""

# for number in range(1, 101):
#     if number % 3 and number % 5:
#         print(number)
#     elif number % 5:
#         print('Fizz')
#     elif number % 3:
#         print('Buzz')
#     else:
#         print('FizzBuzz')

# solution with % 15
for number in range(1, 101):
    if not number % 15:
        print('FizzBuzz')
    elif not number % 5:
        print('Buzz')
    elif not number % 3:
        print('Fizz')
    else:
        print(number)
