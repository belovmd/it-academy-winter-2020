"""Каждый из N школьников некоторой школы знает Mi языков.
   Определите, какие языки знают все школьники и языки,
   которые знает хотя бы один из школьников.
   Входные данные:
   Первая строка входных данных содержит количество школьников N.
   Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
   содержащих названия языков, которые знает i-й школьник.
"""

language = set()
language_s = set()

for i in range(int(input())):
    num = int(input())
    lan = {input() for j in range(num)}
    language_s.update(lan)
    if i == 1:
        language.update(lan)
    else:
        language &= lan

print(len(language))
print('\n'.join(language))
print(len(language_s))
print('\n'.join(language_s))
