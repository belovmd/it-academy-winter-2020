"""Dict comprehensions
   Создайте словарь с помощью генератора словарей, так
   чтобы его ключами были числа от 1 до 20,
   а значениями кубы этих чисел.
"""


a = 1
b = []
while a <= 20:
    b.append(a)
    a = a + 1

dct = {i: i ** 3 for i in b}
print(dct, type(dct))
