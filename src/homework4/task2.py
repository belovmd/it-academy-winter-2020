# Города
# Дан список стран и городов каждой страны. Затем даны
# названия городов. Для каждого города укажите, в какой
# стране он находится.
base_city_country = {}
result_list = []

num_of_countries = int(input('Введите количество стран: '))

for element in range(num_of_countries):
    country, *cities = input("Введите страну и города: ").split()
    for one_city in cities:
        base_city_country[one_city] = country

num_of_requests = int(input('Введите количество запросов: '))

for _ in range(num_of_requests):
    city_to_search = input('Введите город: ')
    found_country = base_city_country[city_to_search]
    result_list.append(found_country)

for city in result_list:
    print(city)
