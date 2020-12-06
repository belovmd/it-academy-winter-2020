"""
    Task 1. Напишите программу, которая считает общую цену.

    Вводится M рублей и N копеек цена, а также количество S товара
    Посчитайте общую цену в рублях и копейках за L товаров.
"""


rubles = int(input("Введите рубли: "))
kopecks = int(input("Введите копейки: "))
quantity = int(input("Введите количество: "))

total = (rubles * 100 + kopecks) * quantity
rubles, kopecks = total // 100, total % 100

print(f"Общая цена {rubles} рублей {kopecks} копеек")
