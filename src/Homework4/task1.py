'''
Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел.
'''

dict_ = {_: _ ** 3 for _ in range(1, 21)}
print(dict_)
