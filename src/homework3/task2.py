import copy


"""
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
"""


list1 = [element1 + element2 for element1 in ['a', 'b'] for element2 in ['b', 'c', 'd']]
print(list1)


"""
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
"""


print(list1[:5:2])


"""
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
"""


list2 = [element + 'a' for element in '1234']
print(list2)


"""
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
"""


print(list2.pop(1))


"""
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""


new_list2 = copy.copy(list2)
new_list2.append('2a')
print(new_list2)
print(list2)

