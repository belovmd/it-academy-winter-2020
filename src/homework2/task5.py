# формала числа фибоначчи F_n = F_{n-1} + F_{n-2}
Number1 = 0
Number2 = 1
print("Ваша последовательность Фибоначчи будет вычислена после ввода числа:")
digit_to_enter = int(input())

print(Number1, end=' ')
print(Number2, end=' ')
for i in range(2, digit_to_enter):
    Number1, Number2 = Number2, Number1 + Number2
    print(Number2, end=' ')




