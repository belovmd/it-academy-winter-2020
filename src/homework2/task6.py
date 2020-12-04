"""Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
   Число положительное целое, произвольной длины.
   Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
"""


num = 12321
temp_num = num
reverse_num = 0

while temp_num:
    digit = temp_num % 10
    reverse_num = reverse_num * 10 + digit
    temp_num //= 10

if num == reverse_num:
    print('yes')
else:
    print('no')
