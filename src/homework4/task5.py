"""Каждый из N школьников некоторой школы знает Mi языков.
   Определите, какие языки знают все школьники и языки,
   которые знает хотя бы один из школьников.
   Входные данные:
   Первая строка входных данных содержит количество школьников N.
   Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
   содержащих названия языков, которые знает i-й школьник.
"""

language = set()
all_languages = set()

for pupils in range(int(input())):
    num_language = int(input())
    pupils_lang = {input() for _ in range(num_language)}
    all_languages.update(pupils_lang)
    if pupils == 1:
        language.update(pupils_lang)
    else:
        language &= pupils_lang

print(len(language))
print('\n'.join(language))
print(len(all_languages))
print('\n'.join(all_languages))
