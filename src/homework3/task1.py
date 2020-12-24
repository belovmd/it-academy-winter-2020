""" #1 Напишите программу, которая печатает цифры от 1 до 100,
   но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный
   5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""

lst = []
for number in range(1, 101):
    if number % 15 == 0:
        lst.append('FizzBuzz')
    elif number % 3 == 0:
        lst.append('Fizz')
    elif number % 5 == 0:
        lst.append('Buzz')
    else:
        lst.append(number)
print(lst)
