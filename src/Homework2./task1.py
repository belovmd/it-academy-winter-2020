'''
Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S
товара Посчитайте общую цену в рублях и копейках за L товаров.
'''
rubles = int(input('Цена в рублях: '))
penny = int(input('Цена в копейках: '))
product = int(input('Количество товара: '))
rubles_product = rubles * product
penny_product = penny * product
print(str(rubles_product) + 'p.' + str(penny_product) + 'k')
