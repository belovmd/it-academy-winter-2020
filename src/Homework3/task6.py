'''
Дан список целых чисел.Требуется переместить все ненулевые
элементы в левую часть списка, не меняя их порядок,
а все нули - в правую часть. Порядок ненулевых элементов
изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
'''
list_1 = [0, 1, 2, 3, 0, 4, ]
for el in list_1:
    if el == 0:
        list_1.remove(el)
        list_1.append(el)
print(list_1)
