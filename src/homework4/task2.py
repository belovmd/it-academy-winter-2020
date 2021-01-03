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
    country_count = 4

    country_with_cities = [
        ('Russia', 'Moscow', 'Petersburg', 'Novgorod', 'Kaluga', ),
        ('Ukraine', 'Kiev', 'Donetsk', 'Odessa', ),
        ('France', 'Paris', 'Lion', 'Brest', ),
        ('Belarus', 'Hrodno', 'Minsk', 'Brest', 'Vitebsk', ),
    ]

    query_count = 4

    queries = [
        "Odessa",
        "Moscow",
        "Novgorod",
        'Brest',
    ]

    city_country_dict = {tuple(cities): country for country, *cities in country_with_cities}

    for query in queries:
        for cities in city_country_dict.keys():
            if query in cities:
                print(city_country_dict[cities], end=' ')
        print()
