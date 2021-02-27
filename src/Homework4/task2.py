'''
Дан список стран и городов каждой страны. Затем даны названия
городов. Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N
строк, каждая строка начинается с названия страны, затем идут
названия городов этой страны. В следующей строке записано
число M, далее идут M запросов — названия каких-то M городов,
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
'''

countries_cities = {}
n_country = int(input('Введите кол-во стран: '))

for i in range(n_country):
    country_cities = input('Введите страну и города:').split(' ')
    countries_cities[country_cities[0]] = country_cities[1:]

n_sities = int(input('Введите кол-во городов: '))
cities = []

for i in range(n_sities):
    cities.append(input('Введите городов:'))

for city in cities:
    for country, data in countries_cities.items():
        if city in data:
            print(country)
