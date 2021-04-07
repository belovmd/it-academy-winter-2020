'''
Оформите указанную задачу из прошлых домашних в виде функции
и покройте тестами. Учтите, что в функцию могут быть переданы
некорректные значения, здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все
возможные ситуации сама.
'''
import json
import os


def get_country_cities(*country_cities):
    countries_cities = {}

    for country_city in country_cities:
        result = country_city.split(' ')
        countries_cities[result[0]] = result[1:]

    return countries_cities


def get_countries(country_cities, *cities):
    result = []

    for city in cities:
        for country, data in country_cities.items():
            if city in data:
                result.append(country)

    return result


def save_countries(filename, countries):
    with open(f'{filename}.txt', 'w') as file:
        json_country_cities = json.dumps(countries)
        file.write(json_country_cities)


def read_countries(filename):
    with open(f'{filename}.txt') as file:
        countries = file.read()
    return json.loads(countries)


if __name__ == '__main__':

    filename = 'countries'
    country_cities = {}

    if os.path.exists(f'{filename}.txt'):
        country_cities = read_countries(filename)
        print(country_cities)
        print('\n')
    else:
        n_country = int(input('Введите колличество стран: '))
        lst = [input('страну и города: ') for i in range(n_country)]
        country_cities = get_country_cities(*lst)

        save_countries(filename, country_cities)

    n_cities = int(input('Введите колличество городов: '))
    cities = [input('Введите город: ') for i in range(n_cities)]

    countries = get_countries(country_cities, *cities)

    print('\n')
    print('\n'.join(countries))
