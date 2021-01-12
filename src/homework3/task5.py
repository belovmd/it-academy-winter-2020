# Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке, в котором
# они встречаются в списке.
list_all = [2, 4, 2, 'a', 5, 'a', 7, 6, 6, 6]
dct_list_all = {}
result = ''
for el in list_all:
    dct_list_all[el] = dct_list_all.get(el, 0) + 1

for key, value in dct_list_all.items():
    if value == 1:
        print(key)
