"""Города
   Дан список стран и городов каждой страны. Затем даны названия городов.
   Для каждого города укажите, в какой стране он находится.
   Входные данные
   Программа получает на вход количество стран N. Далее идет N строк, каждая
   строка начинается с наз-я страны, затем идут наз-я городов этой страны.
   В следующей строке записано число M, далее идут M запросов — названия
   каких-то M городов, перечисленных выше.
   Выходные данные
   Для каждого из запроса выведите название страны, в котором находится
   данный город.
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


n = int(input('Введите кол-во стран: '))
for i in range(n):
    capitals = input('Введите ' + str(i + 1) + ' -ю страну и ее города: ')
    a = capitals.split()
m = int(input('Введите кол-во городов: '))
for j in range(m):
    cities = input('Введите ' + str(j + 1) + ' -й город: ')
    for k in cities:  # ИСПРАВИТЬ !!! не работает
        if cities in a:
            print(a[0])


"""N = int(input('Введите кол-во стран: '))
Rus = 'Russia: Moscow, Petersburg, Novgorod, Kaluga'
Ukr = 'Ukraine: Kiev, Donetsk, Odessa'
Bel = 'Belarus: Minsk, Brest, Lida'
if N == 1:
    print(Rus)
elif N == 2:
    print(Rus)
    print(Ukr)
else:
    print(Rus)
    print(Ukr)
    print(Bel)
M = int(input('Введите кол-во городов: '))
cities = input('Укажите любые города из списка через пробел: ')

a = cities.split()
for i in a:
    if i in Rus:
        print('Russia')
    elif i in Ukr:
        print('Ukraine')
    elif i in Bel:
        print('Belarus')
    else:
        print('Проверьте правильность написания названия города')
"""
