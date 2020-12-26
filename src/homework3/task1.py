"""
    Task 1. FizzBuzz

    Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
    кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
    одновременно кратных и 3 и 5 - FizzBuzz

    Выводит до 100 включительно
"""

start = 1
end = 100

for num in range(start, end + 1):
    fizz = "Fizz" if not num % 3 else ""
    buzz = "Buzz" if not num % 5 else ""
    print(f"{fizz}{buzz}" or num)
