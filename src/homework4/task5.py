""" Fixed
5. Языки
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
"""

n = int((input("Количество школьников: ")))
languages_list = []
all_languages = set()

for student in range(n):
    student_languages = set()
    languages_number = int(input('Введите количество языков: '))
    for language in range(languages_number):
        languages = str(input('Введите язык: '))
        student_languages.add(languages)
        all_languages.add(languages)
    languages_list.append(student_languages)

common_languages = set.intersection(*languages_list)
all_known_languages_number = 0
for element in common_languages:
    all_known_languages_number += 1
print("Все школьники знают"
      " " + str(all_known_languages_number) + " язык(а/ов).")
for element in common_languages:
    print(element)

all_languages_list = list(all_languages)

print("Количество языков, которые знает хотя бы один "
      "школьник: " + str(len(all_languages)) + " язык(а/ов).")
for element in all_languages:
    print(element)
