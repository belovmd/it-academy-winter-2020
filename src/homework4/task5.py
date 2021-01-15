"""
Языки
Каждый из N школьников некоторой школы знает Mi языков.
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
которые знает хотя бы один школьник, на следующих строках -
список таких языков.
"""
languages = set()
all_languages = set()
common_languages = set()
for pupil in range(int(input())):
    for num_lang in range(int(input())):
        i_speak = input()
        languages.add(i_speak)
        all_languages.add(i_speak)
    if not len(common_languages):
        common_languages.update(languages)
    else:
        common_languages = common_languages & languages
    languages.clear()
print(len(common_languages))
for element in common_languages:
    print(element)
print(len(all_languages))
for element in all_languages:
    print(element)
