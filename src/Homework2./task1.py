'''
Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S
товара Посчитайте общую цену в рублях и копейках за L товаров.
'''
rubles = 0
penny = 90
product = 9
penny_product = (penny * product) % 100
rubles_product = (product * rubles) + (product * penny) // 100
print(rubles_product, 'p.', penny_product, 'k.')
