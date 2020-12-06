""" Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится
"""


n = int(input('Введите n-ое число Фибоначчи: '))
number1 = 0
number2 = 1
for i in range(1, n):
    number1, number2 = number2, number1 + number2
print(number2)
