"""
    Task 3. Tuple practice


    Task 3-1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж
"""
tuple_elements = tuple(['a', 'b', 'c'])
print("3-1", tuple_elements)


"""
    Task 3-2. Создайте кортеж ('a', 'b', 'c') и сделайте из него список
"""
list_elements = ('a', 'b', 'c')
print("3-2", list(list_elements))


"""
    Task 3-3. Сделайте следующие присвоения одной строкой
    a = 'a', b=2, c='python'
"""
a, b, c = 'a', 2, 'python'


"""
    Task 3-4. Создайте кортеж из одного элемента, чтобы при итерировании по
    этому элементу последовательно выводились значения 1, 2, 3.
    Убедитесь что len() исходного кортежа возвращает 1.
"""
tuple_elms = ([1, 2, 3], )

print("3-4 length:", len(tuple_elms))

for el in tuple_elms:
    print(*el, sep=", ")
