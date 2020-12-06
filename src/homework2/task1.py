"""
1. Напишите программу, которая считает общую цену.

Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""

M = int(input('Сколько стоит вещь? '
              'Введите сначала рубли, а затем копейки. \nРубли: '))
N = int(input('Копейки: '))
S = int(input('Количество вещей: '))

total_roubles = M * S
total_coins = N * S
if total_coins >= 100:
    total_roubles = total_roubles + total_coins // 100
    total_coins = total_coins - total_coins // 100 * 100

print('Общая стоимость ' + str(total_roubles)
      +' руб. ' + str(total_coins) + ' коп.')
