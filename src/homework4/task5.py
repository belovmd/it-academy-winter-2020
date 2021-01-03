""" Task 5: Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Входные данные:

Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.

"""

from functools import reduce

if __name__ == "__main__":

    # id школьника: его языки
    pupils_lang = {
        1: ('Ru', 'En', ),
        2: ('Ru', 'Be', 'En', ),
        3: ('Ru', 'Fr', 'It',),
    }

    languages = [set(lang_) for lang_ in pupils_lang.values()]

    all_knows_lang = reduce(lambda x, y: x & y, languages)

    one_knows_lang = reduce(lambda x, y: x | y, languages)

    print(f'Кол-во языков которые знают все школьники: {len(all_knows_lang)}\n{" ".join(all_knows_lang)} ')
    print(f'Кол-во языков которые знает хотя бы один из школьников: {len(one_knows_lang)}\n{" ".join(one_knows_lang)}')
