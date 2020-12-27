""" Task 7: Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий
делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

if __name__ == "__main__":
    first_number = 50
    second_number = 130

    while first_number and second_number:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number

    print(f"НОД равен {first_number + second_number}")
