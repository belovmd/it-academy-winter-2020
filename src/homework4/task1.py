"""
    Task 1. Dict comprehensions.

    Создайте словарь с помощью генератора словарей, так чтобы его ключами были
    числа от 1 до 20, а значениями кубы этих чисел.
"""


startNum = 1
endNum = 20

cubes = {num: num ** 3 for num in range(startNum, endNum + 1)}
print(cubes)
