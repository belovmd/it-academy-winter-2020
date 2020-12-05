"""Определите, является ли число палиндромом (читается слева направо и справа
   налево одинаково).  Число положительное целое, произвольной длины. Задача
   требует работать только с числами (без конвертации числа в строку или
   что-нибудь еще)
"""

number = int(input('Введите число '))
reversed_number = 0
tmp_number = number

while tmp_number > 0:
    reversed_number = (reversed_number*10) + tmp_number % 10
    tmp_number = tmp_number // 10
if number == reversed_number:
    print('Палиндром')
else:
    print('Не палиндром')
