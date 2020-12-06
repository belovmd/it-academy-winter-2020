"""Определите, является ли число палиндромом
   (читается слева направо и справа налево одинаково).
   Число положительное целое, произвольной длины.
   Задача требует работать только с числами
   (без конвертации числа в строку или что-нибудь еще)
"""

num = int(input("Please enter your number:"))
temp_num = num
digit_pos = 0
while num > 0:
    digit = num % 10
    digit_pos = digit_pos * 10 + digit
    num = num // 10
if temp_num == digit_pos:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
