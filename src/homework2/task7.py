"""1. Вам дано положительное целое число. Определите сколько цифр оно имеет.
    Входные данные: Положительное целое число.
    Выходные данные: Целое число.
"""


num = 1000
number_length = 0

while num:
    num //= 10
    number_length += 1

print(number_length)


"""2. Попробуйте выяснить какое количество нулей содержит
    данное число в конце.
    Входные данные: Положительное целое число (int).
    Выходные данные: Целое число (int).
"""


num = 10000
end_zeros = 0

while num % 10 == 0:
    num //= 10
    end_zeros += 1

print(end_zeros)


"""3. Вам дана строка состоящая только из цифр.
    Вам нужно посчитать сколько нулей ("0") находится в начале строки.
    Входные данные: Строка, состоящая только из цифр.
    Выходные данные: Целое число.
    Строка может иметь цифры: 0-9.
"""


str_ = '001090650'
count_zeros = 0

for number in str_:
    if number == str('0'):
        count_zeros += 1
    else:
        break

print(count_zeros)


"""4. Given a year, determine whether it is a leap year.
    If it is a leap year, return the Boolean True, otherwise return False.
"""


year = int(input())


def is_leap():
    if year % 4 == 0 and year % 100:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


print(is_leap())
