"""Напишите программу,которая считает общую цену. Вводится M рублей и N копеек
   цена, а также количество S товара Посчитайте общую цену в рублях и копейках
   за L товаров
"""


pricerub = int(input())
pricekop = int(input())
num = int(input())
cost = num * (100 * pricerub + pricekop)
print(cost // 100, 'руб', cost % 100, 'коп')
