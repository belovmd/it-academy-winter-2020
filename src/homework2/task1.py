"""
Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""

M = 3
N = 99
L = 10
total_M = L * M
total_N = L * N

if total_N >= 100:
    total_M += total_N // 100
    total_N = total_N % 100

print('Общая цена', total_M, 'рублей', total_N, 'копеек')
