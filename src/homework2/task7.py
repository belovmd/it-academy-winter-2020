""" #1 Верните данную строку в перевернутом виде.
"""

string = input("Введите строку: ")
reversed_string = string[::-1]
print(reversed_string)


""" #2 У вас есть число и нужно определить какая цифра из этого числа
   является наибольшей.
"""

number = int(input("Введите число: "))
max_digit = max([int(i) for i in str(number)])
print(max_digit)


""" #3 Проверить является ли число четным или нет. Ваша функция должна
   возвращать True если число четное, и False если число не четное.
"""

num = int(input('Введите число '))
if num % 2 == 0:
    print(True)
else:
    print(False)


"""#4 Попробуйте выяснить какое количество нулей содержит данное число в конце
"""

n = int(input('Введите число '))
n_zero = 0
while (n % 10 == 0):
    n //= 10
    n_zero += 1
print(n_zero)


""" #5 Учитывая год, определите, является ли он високосным.
   Если это високосный год, верните логическое значение True,
   в противном случае верните False.
"""

year = int(input('Введите год '))
if year % 4 == 0 and year % 100:
    print(True)
elif year % 400 == 0:
    print(True)
else:
    print(False)


""" 2 additional advanced tasks for higher score
   #1 Учитывая массив целых чисел любой длины, верните массив,
   в который добавлена 1 к значению, представленному массивом.
   массив не может быть пустым
   Разрешены только неотрицательные, однозначные целые числа
   Верните nil (или эквивалент на вашем языке) для недопустимых вводов.
   Примеры:
   Например, массив [2, 3, 9] равен 239, добавление единицы вернет
   массив [2, 4, 0]. [4, 3, 2, 5] вернет [4, 3, 2, 6]
"""


def up_array(arr):
    if not len(arr):
        return None

    for i in arr:
        if 0 < i < 9:
            return None

    num = int(''.join(map(str, arr)))
    num = num + 1

    up_arr = []

    for i in str(num):
        up_arr.append(int(i))

    return up_arr


""" # 2Напишите функцию, которая принимает массив из 10 целых чисел(от 0 до 9)
   который возвращает строку этих чисел в форме номера телефона.
   Пример: create_phone_number ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
   возвращает «(123) 456-7890»
"""


def create_number(q):
    first = "".join(map(str, q[0:3]))
    second = "".join(map(str, q[3:6]))
    third = "".join(map(str, q[6:10]))

    return "(" + first + ") " + second + "-" + third
