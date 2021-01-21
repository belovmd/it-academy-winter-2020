""" Task 4: Movies
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
в файле ./data_hw5/ ratings.list.

a.  Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b.  Найдите ТОП250 фильмов и извлеките заголовки.
c.  Программа создает 3 файла  top250_movies.txt – названия файлов,
    ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: если файл не найден, исключение
def read_ratings(file_name, start_pos=28, count=250):
    """Чтение данный IMDB

    :param file_name: имя файлы
    :param start_pos: позиция с которой начинается чтение
    :param count: int. Количество строк, которое необходимо считать
    :return:
    """
    with open(file_name, mode='r') as f:
        for _ in range(start_pos):
            next(f)
        for idx, line in enumerate(f):
            if count == idx or not line:
                break
            distribution, votes, rank, *title, year = line.split()
            yield distribution, \
                  votes, \
                  rank, \
                  ' '.join(title), \
                  int(year[1:-1]) if '/I' not in year else int(year[1:-3])


def count_elements(data=None):
    """Подсчет количества

    :param data: список.
    :return: словарь. Формат: {'элемент': 'количество раз,
    которое элемент встретился'}
    """
    counter = dict()
    for item in data:
        counter[item] = counter.get(item, 0) + 1

    return counter


def build_txt_hist(data=None, filename='no_name.txt'):
    hist_dict = count_elements(data);
    hist_data = list()
    for key in sorted(hist_dict, key=hist_dict.get, reverse=True):
        _value = '+' * hist_dict[key]
        hist_data.append(f'{key} {_value}')

    return hist_data


def build_sns_hist(dataframe, column=None):
    data_count = dataframe[column].value_counts(sort=True, ascending=True)

    print(data_count)
    plt.figure(figsize=(10, 5))
    sns.barplot(data_count.index, data_count.values, alpha=0.8)
    plt.title('Top movies')
    plt.ylabel('Number of Occurrences', fontsize=12)
    plt.xlabel(column, fontsize=12)
    plt.show()


def write_to_file(data=None, filename='default.txt'):
    """Запись в файл итерируемого объекта

    :param data: список
    :param filename: имя результирующего файлы
    :return: None
    """
    with open(filename, mode='a') as file:
        file.write('\n'.join(data))


def main():
    file_name = 'ratings.list'
    # step 1: считываем данные из файлы
    ratings_data = [item for item in read_ratings(file_name)]

    df = pd.DataFrame(data=ratings_data, columns=['Distribution', 'Votes', 'Rank', 'Title', 'Year'])

    # step 2: построение гистограммы годов
    year_data = build_txt_hist([elem[4] for elem in ratings_data])
    write_to_file(year_data, filename='years.txt')
    build_sns_hist(df, column='Year')

    # step 3: построение гистограммы рейтингов
    rating_data = build_txt_hist([elem[2] for elem in ratings_data])
    write_to_file(rating_data, filename='ratings.txt')

    # step 4: запись фильмов в файл
    write_to_file([elem[3] for elem in ratings_data], filename='top250_movies.txt')


if __name__ == "__main__":
    main()
