"""Упорядоченный список.
Дан список целых чисел. Требуется переместить все ненулевые элементы
в левую часть списка, не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список
использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""
a = [int(i) for i in input().split()]
b = 0
for i in range(len(a)):
    if a[i]:
        print(a[i], end=" ")
    else:
        b = b + 1
for i in range(b):
    print(0, end=" ")
