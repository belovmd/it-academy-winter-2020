"""
Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и условные операторы.
n - вводится
"""
n = int(input('Введите номер числа Фибоначчи, которое хотите получить: '))
num1 = 0
num2 = 1
if n >= 1:
    for _ in range(1, n):
        num1, num2 = num2, num1 + num2
    print(num2)
else:
    (print('Число должно быть больше либо равно единице'))
