"""
1. Dict comprehensions
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов,
перечисленных выше.

Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
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

countries_number = int(input('Количество стран: '))
city_to_country = {}
for element in range(countries_number):
    country_cities = input('Страна и города: ').split()
    country_cities_tuple = tuple(country_cities)
    dct = {country_cities_tuple[index]: country_cities_tuple[0] for index in range(1, len(country_cities_tuple))}
    city_to_country.update(dct)

result_list = []
M = int(input('Введите количество городов: '))
for _ in range(M):
    country = city_to_country[input('Введите город: ')]
    result_list.append(country)
for element in result_list:
    print(element)
