"""
    Task 4. В файле хранятся данные с сайта IMDB.
    Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
    Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
    Найдите ТОП250 фильмов и извлеките заголовки.
    Программа создает 3 файла:
    top250_movies.txt – названия фильмов,
    ratings.txt – гистограмма рейтингов,
    years.txt – гистограмма годов.
"""

import re


def top_250():
    my_dict = dict()
    i = 1
    try:
        with open('ratings.list', 'r+')as f:
            while len(my_dict) < 250:
                line = f.readline()
                result = str(re.findall(r'[\s]{6}[^\n]*(\d\.\d)'
                                        r'\s([^\n]*)', line))
                if result != '[]':
                    my_dict[i] = result[3:-2]
                    i += 1
    except FileNotFoundError:
        print('file not found')
    return my_dict


def film(my_dict):
    with open('top250_movies.txt', 'w')as f:
        for keys in my_dict.keys():
            result = (str(re.findall(r'.{7}([^\n]*)\(\d{4}',
                                     my_dict[keys])))[3:-3]
            f.write(str(keys) + ' ' + result + '\n')


def rating(my_dict):
    rating_dict = {}
    for elem in my_dict.values():
        if elem[0:3] in rating_dict:
            rating_dict[elem[0:3]] += 1
        else:
            rating_dict[elem[0:3]] = 1
    with open('ratings.txt', 'w')as f:
        for keys in rating_dict.keys():
            f.write(keys + ' ' + '|' * rating_dict[keys] + '\n')


def years(my_dict):
    years_dict = {}
    for elem in my_dict.values():
        elem = re.findall(r'\((\d{4})', elem)
        if elem[0] in years_dict:
            years_dict[elem[0]] += 1
        else:
            years_dict[elem[0]] = 1
    with open('years.txt', 'w')as f:
        for keys in range(int(min(years_dict.keys())),
                          int(max(years_dict.keys())) + 1):
            if str(keys) in years_dict.keys():
                f.write(str(keys) + ' ' + '|' * years_dict[str(keys)])
                f.write('\n')


func_result = top_250()
film(func_result)
rating(func_result)
years(func_result)
