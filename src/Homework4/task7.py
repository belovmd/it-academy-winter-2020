'''
Оглянемся назад. Числа
Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
'''


a = 36
b = 48

if a != 0 and b != 0:
    if a > b:
        print(a % b)
    else:
        print(b % a)
else:
    print(a + b)
