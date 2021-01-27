"""В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в
    файле ./data_hw5/ ratings.list.
    a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
    b. Найдите ТОП250 фильмов и извлеките заголовки.
    c. Программа создает 3 файла top250_movies.txt  – названия файлов,
    ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


try:
    rating_list = open('./data_hw5/ratings.list')
except FileNotFoundError:
    print("[Errno 2] No such file or directory: './data_hw5/ratings.list'")


# Prepare the table with top 250.
with open('./data_hw5/ratings.list', 'rt') as rl:
    for line in rl:
        txt = rl.readlines()
        top_250 = txt[27:277]

top_250_new = [element.split() for element in top_250]

with open('./data_hw5/top250_movies.txt', 'w') as titles:
    for element in top_250_new:
        title1 = element[3:-1]
        title2 = ' '.join(title1)
        titles.write(title2 + '\n')

with open('./data_hw5/ratings.txt', 'w') as ratings:
    for element in top_250_new:
        rating = element[2]
        ratings.write(rating + '\n')

with open('./data_hw5/years.txt', 'w') as years:
    for element in top_250_new:
        year = element[-1]
        years.write(year + '\n')


# histogram of ratings
# list of ratings and its quantity
dct = {}
with open('./data_hw5/ratings.txt', 'r') as ratings:
    for line in ratings:
        dct[line] = dct.get(line, 0) + 1

num = Counter(dct)
x = list(num.values())
y = list(num.keys())
x_coordinates = np.arange(len(num.keys()))
plt.bar(x_coordinates, x)
plt.xticks(x_coordinates, y)
plt.show()


# histogram of years
dct2 = {}
with open('./data_hw5/years.txt', 'r') as years:
    for year in years:
        dct2[year] = dct2.get(year, 0) + 1

num2 = Counter(dct2)
x2 = list(num2.values())
y2 = list(num2.keys())
x_coordinates2 = np.arange(len(num2.keys()))
plt.bar(x_coordinates2, x2)
plt.xticks(x_coordinates2, y2)
plt.show()
