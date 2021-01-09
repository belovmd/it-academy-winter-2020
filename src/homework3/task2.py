import copy
"""
List practice
Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
"""
final_list = [el1 + el2 for el1 in ['a', 'b'] for el2 in 'bcd']
print(final_list)

"""
Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
"""
new_lst = final_list[::2]
print(new_lst)

"""
Используйте генератор списков чтобы получить следующий
['1a', '2a', '3a', '4a'].
"""
final_list = [el + 'a' for el in '1234']
print(final_list)

"""
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
"""
print(final_list.pop(1))

"""
Скопируйте список и добавьте в него элемент '2a' так,
чтобы в исходном списке этого элемента не было
"""
# copy and deepcopy work in the same way in this case
new_list = copy.copy(final_list)
new_list.append('2a')
print(new_list)
print(final_list)
