# Tuple practice
# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
list_abc = ['a', 'b', 'c']
tpl_list = tuple(list_abc)
print(tpl_list)

# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
list_abc2 = list(tpl_list)
print(list_abc2)

# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
a, b, c = 'a', '2', 'python'
print(a, b, c)

# Создайте кортеж из одного элемента, чтобы при итерировании по этому
# элементы последовательно выводились значения 1, 2, 3. Убедитесь что
# len() исходного кортежа возвращает 1.
tupl_iter = ([1, 2, 3],)
print(len(tupl_iter))

for el in tupl_iter[0]:
    print(el)
