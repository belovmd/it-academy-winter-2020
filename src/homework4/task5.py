"""Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
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
которые знает хотя бы один школьник, на следующих строках - список таких языков.
"""

students1 = 2
students1_lan = ['Russian', 'English']
students2 = 3
students2_lan = ['Russian', 'English', 'Belarusian']
students3 = 3
students3_lan = ['Russian', 'Italian', 'French']


all_lang = set(students1_lan + students2_lan + students3_lan)
print('Всего студенты знают', str(len(all_lang)), 'языков')
print('Список языков которые знают все школьники: ', all_lang)

students_lang = set(students3_lan) - set(students2_lan) - set(students1_lan)
print('Количество языков которые знает хотя бы один школьник:', str(len(students_lang)))
print('список  таких языков:', students_lang)

students_lan1 = set(students2_lan) - set(students3_lan) - set(students1_lan)
print('Количество языков которые знает хотя бы один школьник:', str(len(students_lan1)))
print('список  таких языков:', students_lan1)
