import copy

# List practice
# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
list_orig = [el1 + el2 for el1 in ['a', 'b'] for el2 in ['b', 'c', 'd']]
print(list_orig)

# Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
list_slice = list_orig[::2]
print(list_slice)

# Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
list_num = [str(el1) + el2 for el1 in range(1, 5) for el2 in ['a']]
print(list_num)

# Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
print(list_num.pop(1))
print(list_num)

# Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
# списке этого элемента не было.
list_copy = copy.copy(list_num)
list_copy.append('2a')
print(list_copy)
