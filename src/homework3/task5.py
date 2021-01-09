"""
5. Уникальные элементы в списке
Дан список.
Выведите те его элементы, которые встречаются
в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""

initial_list = [2, 2, 'abc', 79, 'k', 1, 67, 'k']
result_list = []
elements_number = {}
for element in initial_list:
    elements_number[element] = elements_number.get(element, 0) + 1

for key in elements_number:
    if elements_number[key] == 1:
        result_list.append(key)
print(result_list)
