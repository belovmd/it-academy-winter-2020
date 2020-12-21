# 5. Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится
n = 20
fib_num_0 = 0
fib_num_1 = 1

for num in range(1, n):
    fib_num_0, fib_num_1 = fib_num_1, fib_num_0 + fib_num_1

print(fib_num_1)
