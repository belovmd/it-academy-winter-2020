"""
    Task 5. Уникальные элементы в списке

    Дан список. Выведите те его элементы, которые встречаются в списке только
    один раз. Элементы нужно выводить в том порядке, в котором они встречаются
    в списке.
"""

elms = [1, [7], 10, 4, "str", 8, 10, "one more str", 32, 12, "str", [7]]
unique_elms = []

for el in elms:
    if el not in unique_elms:
        unique_elms.append(el)
    else:
        unique_elms.remove(el)

print(*unique_elms, sep=", ")
