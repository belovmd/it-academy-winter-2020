'''
Дан список. Выведите те его элементы, которые встречаются в списке
только один раз. Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
'''
list_1 = [3, 4, 0, 1, 2, 3, 3, ]
for el in list_1:
    list_1.count(el)
    if list_1.count(el) == 1:
        print(el)
