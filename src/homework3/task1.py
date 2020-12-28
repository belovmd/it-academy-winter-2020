# FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5
# пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
start = 1
while start <= 100:
    if not start % 3 and not start % 5:
        print('FizzBuzz')
    elif not start % 5:
        print('Buzz')
    elif not start % 3:
        print('Fizz')
    else:
        print(start)
    start += 1
