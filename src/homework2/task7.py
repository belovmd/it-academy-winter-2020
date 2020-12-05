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


""" #3 Проверить является ли число четным или нет. Ваша функция 
   должна возвращать True если число четное, и False если число не четное.
"""

num = int(input('Введите число '))
if num % 2 == 0:
    print(True)
else:
    print(False)


""" #4 Попробуйте выяснить какое количество нулей содержит данное число в конце.
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
