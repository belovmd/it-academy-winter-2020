"""В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в
    файле ./data_hw5/ ratings.list.
    a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
    b. Найдите ТОП250 фильмов и извлеките заголовки.
    c. Программа создает 3 файла top250_movies.txt  – названия файлов,
    ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""

import matplotlib.pyplot as plt

path_list = 'data_hw5/ratings.list'

try:
    raiting_list = open(path_list, 'r', encoding='ISO-8859-1')
except FileNotFoundError:
    print(f'No such file or directory: {path_list}')

titles = []
ratings = []
years = []

for line in raiting_list:
    if not line.startswith('      '):
        continue

    film = [n for n in line.split(' ') if n != '']
    if len(film) < 5:
        continue

    ratings.append(film[2])
    titles.append(' '.join(film[3:-1]))
    years.append(film[-1][1:5])


def write_file(name, lst):
    with open(name, 'w') as file:
        file.write('\n'.join(lst))


write_file('top250_movies.txt', titles[:250])

num_bins = 25
n, bins, patches = plt.hist(ratings[:250], num_bins)
plt.title('Histogram ratings')
plt.show()

num_bins = 250
n, bins, patches = plt.hist(years[:250], num_bins)
plt.title('Histogram years')
plt.show()
