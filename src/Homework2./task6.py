"""
Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""
num = int(input('Введите число: '))
num_1 = num
new_number = 0
while num_1:
    new_number = (10 * new_number) + num_1 % 10
    num_1 //= 10
if num == new_number:
    print('Палиндром')
else:
    print('Не палиндром')
