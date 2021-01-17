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
Для каждого из запроса выведите название страны,
в котором находится данный город.
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

Пример 2
Входные данные
Количество стран: 2
Страна и города: Франция Брест Париж
Страна и города: Беларусь Брест Минск
Введите количество городов: 2
Введите город: Брест
Введите город: Минск

"""


countries_number = int(input('Количество стран: '))
city_to_country = {}
for element in range(countries_number):
    country_cities = input('Страна и города: ').split()
    country = country_cities[0]
    cities = country_cities[1:]
    for city in cities:
        city_to_country.setdefault(city, []).append(country)

result_list = []
M = int(input('Введите количество городов: '))
for _ in range(M):
    country = city_to_country[input('Введите город: ')]
    result_list.append(country)
for element in result_list:
    print(*element)
