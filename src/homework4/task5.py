# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
all_language = set()
all_language_one = []
language_one = set()

N = int(input('Введите количество школьников: '))
for element in range(N):
    M = int(input('Введите количество языков школьника: '))
    for _ in range(M):
        language = input('Введите язык: ')
        all_language.add(language)
        all_language_one.append(language)

for el in all_language_one:
    if all_language_one.count(el) == N:
        language_one.add(el)
print('Количество языков, которые знают все школьники: ' + str(len(language_one)))

for el in language_one:
    print(el)

print('Количество языков, которые знает хотя бы один школьник: ' + str(len(all_language)))

for el in all_language:
    print(el)
