"""Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.
    Входные данные
    Программа получает на вход количество стран N.
    Далее идет N строк, каждая строка начинается с названия страны,
    затем идут названия городов этой страны. В следующей строке записано
    число M, далее идут M запросов — названия каких-то M городов,
    перечисленных выше.
    Выходные данные
    Для каждого из запроса выведите название страны, в котором находится
    данный город.
    Примеры

    Входные данные
    2
    Russia Moscow Petersburg Novgorod Kaluga
    Ukraine Kiev Donetsk Odessa


    3
    Odessa
    Moscow
    Novgorod

    Выходные данные
    Ukraine
    Russia
    Russia
"""


N = int(input())
dct = {}

while N:
    countries, *cities = input().split()
    N -= 1

    for city in cities:
        dct.setdefault(city, []).append(countries)

M = int(input())

while M:
    city = input()
    print(*dct[city])
    M -= 1
