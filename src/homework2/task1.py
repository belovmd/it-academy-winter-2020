price = float(input("Цена одной вещи:"))
print("Чтобы посчитать стоимость, введите количество товара:")
quantity = int(input())
amount = round(price * quantity, 3)

print(amount)
