"""Уникальные элементы в списке
   Дан список. Выведите те его элементы, которые встречаются в списке
   только один раз. Элементы нужно выводить в том порядке, в котором они
   встречаются в списке.
"""


old_list = [1, 1, 2, 2, 3, 4, 5]
for i in range(len(old_list)):
    for j in range(len(old_list)):
        if i != j and old_list[i] == old_list[j]:
            break
    else:
        print(old_list[i])