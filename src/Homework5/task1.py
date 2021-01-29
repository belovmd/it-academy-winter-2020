"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

"""Задача HW2 : ВВыведите n-ое число Фибоначчи,
 используя только временные переменные,
  циклические операторы и условные операторы.
  """


def fibonacci(n):

    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


if __name__ == '__main__':
    fibonacci(10)


"""Задача HW2: Определите, является ли число палиндромом
 (читается слева направо и справа налево одинаково).
  Число положительное целое, произвольной длины.
   Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""


def reverse_number(n, partial=0):
    if n == 0:
        return partial
    return reverse_number(n // 10, partial * 10 + n % 10)


trial = 123454321

if reverse_number(trial) == trial:
    print("It's a Palindrome!")

if __name__ == '__main__':
    reverse_number(123454321)


"""Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный
5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def fizzbuzz():
    for i in range(1, 101):
        print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)


print(fizzbuzz())


if __name__ == '__main__':
    fizzbuzz()
