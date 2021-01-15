"""
Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""
num_1 = 30
num_2 = 15
bigger_num = 0
while num_1 and num_2:
    if num_1 > num_2:
        num_1 %= num_2
        bigger_num = num_2
    else:
        num_2 %= num_1
        bigger_num = num_1
print(bigger_num)
