"""Дан список стран и городов каждой страны. Затем даны названия городов.
 Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
 Далее идет N строк, каждая строка начинается с названия страны,
  затем идут названия городов этой страны. В следующей строке записано число M,
   далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
"""

dct_ = dict()
Country = []
Cities = []
country_nbr = int(input())                    #количество стран
for i in range(country_nbr):
    list_to_enter = input('Введите строку: ')     #ввод названия страны и городов
    list_ = list_to_enter.split()
    print(list_)
    Country.insert(len(Country), list_[0])  #список стран
    print(Country)
    Cities.insert(len(Cities), list_[1:len(list_)]) #список городов
    print(Cities)

dict_ = dict(zip(Country, Cities)) #словарь
print(dict_)
number_to_check = int(input())                      #количество городов для определения
for i in range(number_to_check):
    city = input('Введите строку: ')         #ввод названия города
    for key, value in dict_.items():             #поиск страны с данным городом
        if city in value:
            print(key)
