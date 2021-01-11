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
languages_1st = ['Russian', 'English']
language_num_2nd = 3
languages_2nd = ['Russian', 'Belarussian', 'English']
language_num_3rd = 3
languages_3rd = ['Russian', 'French', 'Italian']
Quantity_of_languages = len(set(languages_1st + languages_2nd + languages_3rd))
print("Все школьники знают", Quantity_of_languages, "языков)")
List_of_languages = set(languages_1st) & set(languages_2nd) & set(languages_3rd)
print("Список языков, которые знают все школьники", List_of_languages)
at_list_1_pupil = len(set(languages_3rd) - set(languages_1st) - set(languages_2nd))
print("Кол-во языков, которые знает хотя бы один школьник", at_list_1_pupil)
list_at_list_1_pipil = set(languages_3rd) - set(languages_1st) - set(languages_2nd)
print("Например: ", list_at_list_1_pipil)
