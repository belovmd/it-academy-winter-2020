'''
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементы последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
'''

list_ = ['a', 'b', 'c']
print(tuple(list_))

tuple_ = ('a', 'b', 'c')
print(list(tuple_))

a, b, c = 'a', 2, 'pytnon'
print(a, b, c)

tuple_1 = ('1, 2, 3', )
for _ in tuple_1:
    print(_)
