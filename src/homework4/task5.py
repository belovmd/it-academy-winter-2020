"""Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник."""
pupils = [{input() for j in range(int(input()))} for i in range(int(input()))]

every_pupil = set.intersection(*pupils)
someone_pupil = set.union(*pupils)

print(len(every_pupil), *sorted(every_pupil), sep='\n')
print(len(someone_pupil), *sorted(someone_pupil), sep='\n')
