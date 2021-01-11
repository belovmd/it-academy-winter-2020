"""Языки
   Каждый из N школьников некоторой школы знает Mi языков.
   Определите, какие языки знают все школьники и языки,
   которые знает хотя бы один из школьников.
   Выходные данные
   В первой строке выведите количество языков, которые знают все школьники.
   Начиная со второй строки - список таких языков. Затем - количество языков,
   которые знает хотя бы один школьник, на следующих строках-
   список таких языков.
"""


common_language_for_all = set()
all_studied_languages = set()

for i in range(int(input())):
    m = int(input())
    a = {input() for j in range(m)}
    all_studied_languages.update(a)

    if i == 1:
        common_language_for_all.update(a)
    else:
        common_language_for_all &= a

print(len(common_language_for_all))
print('\n'.join(sorted(common_language_for_all)))

print(len(all_studied_languages))
print('\n'.join(sorted(all_studied_languages)))
