"""
    Task 3. Оформите указанную задачу из прошлых домашних в виде функции и
    покройте тестами. Учтите, что в функцию могут быть переданы некорректные
    значения, здесь может пригодится ‘assertRaises’. Не нужно переделывать
    функцию для того чтобы она ловила все возможные ситуации сама.


    Вариант 5.
    Task 5 Homework4. Языки.
    Каждый из N школьников некоторой школы знает Mi языков.
    Определите, какие языки знают все школьники и языки, которые знает хотя бы
    один из школьников.
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
    которые знает хотя бы один школьник, на следующих строках - список таких
    языков.
"""


def students_languages_info():
    """
    Считает какие языки знают все школьники и языки, которые знает хотя бы
    один из школьников

    :return: str. количество языков, которые знают все школьники,
        список таких языков через запятую,
        количество языков, которые знает хотя бы один школьник,
        список таких языков через запятую
    """
    students = int(input("Количество школьников: "))
    languages_known = []

    for student in range(1, students + 1):
        languages = []
        for _ in range(int(input(f"Количество языков школьника {student}: "))):
            languages.append(input(f"Язык школьника {student}: "))

        languages_known.append(languages)

    all_know = set.intersection(*map(set, languages_known))
    all_know_len = len(all_know)

    someone_know = set.union(*map(set, languages_known))
    someone_know_len = len(someone_know)

    prepare_result = ""

    if all_know_len:
        prepare_result += f"{all_know_len}\n{', '.join(all_know)}\n"
    else:
        prepare_result += f"{all_know_len}\n"

    if someone_know_len:
        prepare_result += f"{someone_know_len}\n{', '.join(someone_know)}\n"
    else:
        prepare_result += f"{someone_know_len}\n"

    print(prepare_result)
    return prepare_result


if __name__ == '__main__':
    students_languages_info()
