"""
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится.
"""
fibonacci = int(input('Введите число Фибоначчи: '))
number = 0
number_1 = 1
for i in range(1, fibonacci):
    number, number_1 = number_1, number + number_1
print(number_1)
