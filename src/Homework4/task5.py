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

Nbr_1 = 2       # введите количество языков которые знает первый школьник
language_1 = ['Russian', 'English']
Nbr_2 = 3       # введите количество языков которые знает второй школьник
language_2 = ['Russian', 'Belarussian', 'English']
Nbr_3 = 3       # введите количество языков которые знает третий школьник
language_3 = ['Russian', 'French', 'Italian']
Quantity_of_languages = len(set(language_1 + language_2 + language_3))
print("Все школьники знают", Quantity_of_languages, "языкаов)")
List_of_languages = set(language_1 + language_2 + language_3)
print("Список языков, которые знают все школьники", List_of_languages)
at_list_1_pupil = len(set(language_3) - set(language_1) - set(language_2))
print("Количество языков, которые знает хотя бы один школьник", at_list_1_pupil)
list_at_list_1_pipil = set(language_3) - set(language_1) - set(language_2)
print("Например: ", list_at_list_1_pipil)
