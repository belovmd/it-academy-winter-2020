"""
    Task 5. Уникальные элементы в списке

    Дан список. Выведите те его элементы, которые встречаются в списке только
    один раз. Элементы нужно выводить в том порядке, в котором они встречаются
    в списке.
"""

list_of_numbers = [1, [7], 10, 4, "str", 8, 10, "one more str", 32, 12, "str", [7]]
unique_elements = [el for el in list_of_numbers if list_of_numbers.count(el) == 1]
print(*unique_elements, sep=", ")
