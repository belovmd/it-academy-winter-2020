# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
all_language = set()
all_language_one = set()
language_one = set()

num_students = int(input('Введите количество школьников: '))

for element in range(num_students):
    num_languages = int(input('Введите количество языков школьника: '))
    for _ in range(num_languages):
        language = input('Введите язык: ')
        all_language.add(language)
        all_language_one.add(language)
    if not language_one:
        language_one.update(all_language_one)
        all_language_one.clear()
    else:
        language_one &= all_language_one
        all_language_one.clear()

print('Количество языков, которые знают все '
      'школьники: ' + str(len(language_one)))

for el in language_one:
    print(el)

print('Количество языков, которые знает хотя '
      'бы один школьник: ' + str(len(all_language)))

for el in all_language:
    print(el)
