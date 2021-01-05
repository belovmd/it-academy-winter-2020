'''
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
В первой строке выведите количество языков,
которые знают все школьники. Начиная со второй строки - список
таких языков. Затем - количество языков,
которые знает хотя бы один школьник,
на следующих строках - список таких языков.
'''


lang_ = set()
all_lang = set()

for pupils in range(int(input('количество школьников: '))):
    numb_lang = int(input('количество языков ' + str(pupils + 1) + ' школьника: '))
    lang_pupils = {input('языки ' + str(pupils + 1) + ' школьника: ') for _ in range(numb_lang)}
    all_lang.update(lang_pupils)
    lang_.update(lang_pupils)

    if pupils == 1:
        pass
    else:
        lang_ &= lang_pupils

print('все языки какие знают школьники:', ', '.join(all_lang))

print('язвыки одного из школьников:', ', '.join(lang_))
