"""
    Task 1. Dict comprehensions.

    Создайте словарь с помощью генератора словарей, так чтобы его ключами были
    числа от 1 до 20, а значениями кубы этих чисел.
"""


from_num = 1
to_num = 20

cubes = {num: num ** 3 for num in range(from_num, to_num + 1)}
print(cubes)
