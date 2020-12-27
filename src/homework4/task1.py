"""Task 1: Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его ключами
были числа от 1 до 20, а значениями кубы этих чисел.
"""

if __name__ == "__main__":
    dict_ = {element: element ** 3 for element in range(1, 21)}
    print(dict_)
