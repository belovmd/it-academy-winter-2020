"""Каждый из N школьников некоторой школы знает Mi языков.
    Определите, какие языки знают все школьники и языки,
    которые знает хотя бы один из школьников.

    Входные данные
    Первая строка входных данных содержит количество школьников N.
    Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
    содержащих названия языков, которые знает i-й школьник.
    Пример входных данных:
    3          # N количество школьников
    2          # M1 количество языков первого школьника
    Russian    # языки первого школьника
    English
    3          # M2 количество языков второго школьника
    Russian
    Belarusian
    English
    3
    Russian
    Italian
    French


    Выходные данные
    В первой строке выведите количество языков, которые знают все школьники.
    Начиная со второй строки - список таких языков. Затем - количество языков,
    которые знает хотя бы один школьник, на следующих строках - список
    таких языков.
"""


N = int(input())
languages = []
dct = {}
n = 0

for student in range(N):
    M1 = int(input())
    while M1:
        language = input()
        languages.append(language)
        M1 -= 1

for language in languages:
    dct[language] = dct.get(language, 0) + 1

for value in dct.values():
    if N == value:
        n += 1
print('All students have', n, 'languages in common')

for key in dct.keys():
    if dct[key] == N:
        print('Here they are:', key)

print(len(set(languages)), *set(languages), sep='\n')
