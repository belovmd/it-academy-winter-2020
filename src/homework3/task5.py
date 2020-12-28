# Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке, в котором
# они встречаются в списке.
list_all = [2, 4, 2, 'a', 5, 'a', 7, 6, 6, 6]
result = ''
for el in list_all:
    if list_all.count(el) == 1:
        result += str(el)
while list_all.count(el) > 1:
    list_all.remove(el)
print(result)
