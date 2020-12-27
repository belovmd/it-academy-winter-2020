"""FizzBuzz. Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""

for char in range(1, 101):
    if not char % 15:
        print("FizzBuzz")
    elif not char % 3:
        print("Fizz")
    elif not char % 5:
        print("Buzz")
    else:
        print(char)