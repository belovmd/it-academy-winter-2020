"""
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
"""


list_ = ['a', 'b', 'c', ]
tuple_ = tuple(list_)
print(tuple_)


"""
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
"""


tuple1 = ('a', 'b', 'c')
list1 = list(tuple1)
print(list1)


"""
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
"""


a, b, c = 'a', 2, 'python'
print(a, b, c)


"""
Создайте кортеж из одного элемента, чтобы при итерировании по 
этому элементы последовательно выводились значения 1, 2, 3
Убедитесь что len() исходного кортежа возвращает 1.
"""


tuple_ = ([1, 2, 3, ],)
print(len(tuple_))
for element in tuple_[0]:
    print(element, end=' ')
