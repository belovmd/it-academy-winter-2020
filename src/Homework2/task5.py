"""Выведите n-ое число Фибоначчи,
   используя только временные переменные,
   циклические операторы и условные операторы"""

# формула числа фибоначчи F_n = F_{n-1} + F_{n-2}
Number1 = 0
Number2 = 1
print("Ваша последовательность Фибоначчи будет вычислена после ввода числа:")
digit_to_enter = int(input())

print(Number1)
print(Number2)
for i in range(2, digit_to_enter):
    Number1, Number2 = Number2, Number1 + Number2
    print(Number2)