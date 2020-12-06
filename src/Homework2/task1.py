'''
Напишите программу, которая считает общую цену. 
Вводится M рублей и N копеек цена, а также количество S 
товара Посчитайте общую цену в рублях и копейках за L товаров.
'''
maney = int(input('Цена в рублях: '))
maney_1 = int(input('Цена в копейках: '))
product = int(input('Количество товара: '))
maney_product = maney * product
maney_1_product = maney_1 * product
print(str(maney_product) + 'p.' + str(maney_1_product) + 'p')
