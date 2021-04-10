"""В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в
    файле ./data_hw5/ ratings.list.
    a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
    b. Найдите ТОП250 фильмов и извлеките заголовки.
    c. Программа создает 3 файла top250_movies.txt  – названия файлов,
    ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""

import matplotlib.pyplot as plt

PATH_DATA_HW5 = '~/data_hw5'
PATH_RATING_LIST = f'{PATH_DATA_HW5}/ratings.list'

try:
    raiting_list = open(PATH_RATING_LIST, 'r', encoding='ISO-8859-1')
except FileNotFoundError:
    print(f'No such file or directory: {PATH_RATING_LIST}')

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


write_file(f'{PATH_DATA_HW5}/top250_movies.txt', titles[:250])

num_bins = 25
n, bins, patches = plt.hist(ratings[:250], num_bins)
plt.title('Histogram ratings')
plt.show()

num_bins = 250
n, bins, patches = plt.hist(years[:250], num_bins)
plt.title('Histogram years')
plt.show()
