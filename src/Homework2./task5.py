"""
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится.
"""
fibonacci = int(input(': '))
num_1 = 0
num_2 = 1
for num_ in range(1, fibonacci):
    num_1, num_2 = num_2, num_1 + num_2
print(num_2)
