""" Дан список. Выведите те его элементы, которые встречаются
   в списке только один раз. Элементы нужно выводить в том порядке,
   в котором они встречаются в списке.
"""

lst = ['a', 'b', 'c', 'c', 13, 3, 3, 14]
dct = {}
for element in lst:
    dct[element] = dct.get(element, 0) + 1
for key, value in dct.items():
    if value == 1:
        print(key)
