""" Task 2: Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные:

Программа получает на вход количество стран N. Далее идет N строк, каждая
строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия
каких-то M городов, перечисленных выше.

Выходные данные:

Для каждого из запроса выведите название страны, в котором находится
данный город.
"""

if __name__ == "__main__":
    country_with_cities = [
        ('Russia', 'Moscow', 'Petersburg', 'Novgorod', 'Kaluga',),
        ('Ukraine', 'Kiev', 'Donetsk', 'Odessa',),
        ('France', 'Paris', 'Lion', 'Brest',),
        ('Belarus', 'Hrodno', 'Minsk', 'Brest', 'Vitebsk',),
    ]

    queries = [
        "Odessa",
        "Moscow",
        "Novgorod",
        'Brest',
    ]

    _dict_city_country = dict()

    for country, *cities in country_with_cities:
        for city in cities:
            if city in _dict_city_country:
                _dict_city_country[city] = \
                    _dict_city_country[city] + (country,)
            else:
                _dict_city_country[city] = (country,)

    for query in queries:
        if query in _dict_city_country:
            print(*_dict_city_country[query])
