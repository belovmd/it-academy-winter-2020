"""Города
   Дан список стран и городов каждой страны. Затем даны названия городов.
   Для каждого города укажите, в какой стране он находится.
   
   Входные данные
   Программа получает на вход количество стран N. Далее идет N строк,
   каждая строка начинается с наз-я страны, затем идут наз-я городов
   этой страны. В следующей строке записано число M, далее идут M
   запросов — названия каких-то M городов, перечисленных выше.
   
   Выходные данные
   Для каждого из запроса выведите название страны, в котором
   находится данный город.
   
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


capitals_cities = {}
n = int(input('Введите кол-во стран: '))
for i in range(n):
    capitals = input('Введите ' + str(i + 1) + ' -ю страну и ее города: ')
    a = capitals.split()
    capital = a[0]
    cities = a[1:]
    for k in cities:
        capitals_cities[k] = capital
        
m = int(input('Введите кол-во городов: '))
for j in range(m):
    city = input('Введите ' + str(j + 1) + ' -й город: ')
    print(capitals_cities[city])
