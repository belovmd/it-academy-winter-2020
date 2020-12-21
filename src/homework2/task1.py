# 1. Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество S товара.
# Посчитайте общую цену в рублях и копейках за L товаров.
rubl = int(input('Введите стоимость в рублях: '))
cent = int(input('Введите стоимость в копейках: '))
count = int(input('Введите количество товаров: '))
all_rubl = rubl * count
all_cent = cent * count
ost_cent = all_cent % 100
integer_cent = all_cent // 100

if all_cent > 99:
    all_rubl = all_rubl + integer_cent

if all_cent > 99:
    print(f'Общая стоимость товаров {all_rubl} руб {ost_cent} центов')
else:
    print(f'Общая стоимость товаров {all_rubl} руб {all_cent} центов')
