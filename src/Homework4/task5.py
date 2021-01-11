""" Первая строка входных данных содержит количество школьников N.
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


language_num_1st = 2
languages1st = ['Russian', 'English']
language_num_2nd = 3
languages2nd = ['Russian', 'Belarussian', 'English']
language_num_3rd = 3
languages3rd = ['Russian', 'French', 'Italian']
quantity_of_languages = len(set(languages1st + languages2nd + languages3rd))
print("Все школьники знают", quantity_of_languages, "языков)")
list_of_languages = set(languages1st) & set(languages2nd) & set(languages3rd)
print("Список языков, которые знают все школьники", list_of_languages)
_pupil_1 = len(set(languages3rd) - set(languages1st) - set(languages2nd))
print("Кол-во языков, которые знает хотя бы один школьник", _pupil_1)
at_list_1_pupil = set(languages3rd) - set(languages1st) - set(languages2nd)
print("Например: ", at_list_1_pupil)
