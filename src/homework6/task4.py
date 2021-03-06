# Рассмотрим число 15.
# Существует восемь положительных целых чисел меньше 15,
# которые являются взаимно простыми с 15: 1, 2, 4, 7, 8, 11, 13, 14.
# Числами, обратными этим восьми по модулю 15, являются:
# 1, 8, 4, 13, 2, 11, 7, 14
# так как
# 1*1 mod 15=1
# 2*8=16 mod 15=1
# 4*4=16 mod 15=1
# 7*13=91 mod 15=1
# 11*11=121 mod 15=1
# 14*14=196 mod 15=1
# Пусть I(n) будет наибольшим положительным числом m меньше
# n-1, таким что число, обратное числу m по модулю n равно
# самому же m .
# Таким образом, I(15)=11.
# Также, I(100)=51 и I(7)=1.
# Найдите ∑I(n) для 3≤n≤2·107
"""Функция находит максимальное число в диапазоне от 1 до module - 1,
равное обратному по модулю от него же"""


def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1


gen = infinite_sequence()


def func(module_):
    all_result = list()
    while True:
        reverse_number = next(gen)
        if reverse_number < module_ - 1:
            result = reverse_number * reverse_number
            if result % module_ == 1:
                all_result.append(reverse_number)
            else:
                continue
        else:
            break
    return max(all_result)


print(func(100))
