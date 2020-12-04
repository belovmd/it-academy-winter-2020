"""Выведите n-ое число Фибоначчи, используя только временные переменные,
   циклические операторы и условные операторы. n - вводится.
"""


n = int(input())
num_1 = 0
num_2 = 1

if n == 1:
    print(num_1)

else:
    while n - 2:
        sum_num = num_1 + num_2
        num_1, num_2 = num_2, sum_num
        n -= 1

    print(num_2)
