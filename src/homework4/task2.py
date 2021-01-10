# Города
# Дан список стран и городов каждой страны. Затем даны
# названия городов. Для каждого города укажите, в какой
# стране он находится.
all_base_dct = {}
result_list = []
N = int(input('Введите количество стран: '))

for element in range(N):
    countries_cities = input("Введите страну и города: ").split()
    all_base_dct[countries_cities[0]] = \
        countries_cities[1:len(countries_cities)]
    # countries_cities[1:len(countries_cities)] - слайс городов
    # для добавления в словарь
M = int(input('Введите количество запросов: '))

for _ in range(M):
    cities = input('Введите город: ')
    for key, value in all_base_dct.items():
        if cities in value:
            result_list.append(key)

for city in result_list:
    print(city)
