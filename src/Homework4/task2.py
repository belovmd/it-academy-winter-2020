'''
Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
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
'''


all_ctr = []
all_city = []
for _ in range(int(input('число стран: '))):
    city_name = input('названия страны и городов этой страны: ').split()
    all_ctr.insert(len(all_ctr), city_name[0])
    all_city.insert(len(all_city), city_name[1: len(city_name)])

dct_ = dict(zip(all_ctr, all_city))

for _ in range(int(input('количество M городов или стран которых нужно вывести: '))):
    city = input('названия каких-то M города или страны: ')
    for key, value in dct_.items():
        if city in value:
            print(key)
