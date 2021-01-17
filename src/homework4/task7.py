"""
    Task 7. Оглянемся назад. Числа.

    Даны два натуральных числа. Вычислите их наибольший общий делитель при
    помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""


num1 = 32
num2 = 12
divider = 0

while num1 and num2:
    if num1 > num2:
        num1 = num1 % num2
    elif num1 < num2:
        num2 = num2 % num1

divider = num1 if num1 > num2 else num2

print(f"Наибольший общий делитель - {divider}")
