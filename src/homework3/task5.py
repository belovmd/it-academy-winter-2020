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
for element in initial_list:
    if initial_list.count(element) == 1:
        result_list.append(element)
print(result_list)
