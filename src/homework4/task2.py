"""
    Task 2. Города.

    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.

    Входные данные
    Программа получает на вход количество стран N. Далее идет N строк, каждая
    строка начинается с названия страны, затем идут названия городов этой
    страны. В следующей строке записано число M, далее идут M запросов —
    названия каких-то M городов, перечисленных выше.

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


def get_countries():
    state = {}
    requested_cities = []

    for _ in range(int(input("Количество стран: "))):
        country, *cities = input("Страна, города: ").split()
        state[country] = cities

    for _ in range(int(input("Количество запрашиваемых городов: "))):
        requested_cities.append(input("Город: "))

    for city in requested_cities:
        print(*[key for key in state if city in state[key]])


get_countries()
