""" Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
    а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров"""

price = float(input("Цена одной вещи:"))
print("Чтобы посчитать стоимость, введите количество товара:")
quantity = int(input())
amount = round(price * quantity, 3)

print(amount)
