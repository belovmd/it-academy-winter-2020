"""
Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""


namb = int(input("Введите целое число: "))
namb_1 = namb
num = 0
while namb_1 > 0:
    num = (10 * num) + namb_1 % 10
    namb_1 //= 10


if namb == num:
    print('число является палиндромом')
else:
    print('число не является палиндромом')
