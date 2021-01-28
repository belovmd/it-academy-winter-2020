"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
 years.txt – гистограмма годов.
"""


from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

my_file = open('C:/Users/Lenovo/Desktop/PYTHON/HW5/ratings.list', 'r+')
try:
    for line in my_file:
        if line in range(28, 278):
            my_file.readlines()
except FileNotFoundError:
    print("No file found in the indicated directory")


top_250_movies = [element.split for element in my_file.readlines()]


with open('C:/Users/Lenovo/Desktop/PYTHON/HW5/top250_movies.txt', 'w+') as film_titles:
    for element in top_250_movies:
        title1 = element[3:0:-1]
        title2 = ' '.join(title1)
        film_titles.write(title2 + '\n')

with open('C:/Users/Lenovo/Desktop/PYTHON/HW5/ratings.txt', 'w+') as ranks_doc:
    for element in top_250_movies:
        rank = element[:2]
        ranks_doc.write(rank + '\n')

    dct = {}
    for line in ranks_doc:
        dct[line] = dct.get(line, 0) + 1
    print(dct)

    num = Counter(dct)
    x = list(num.values())
    y = list(num.keys())
    x_coordinates = np.arange(len(num.keys()))
    plt.bar(x_coordinates, x)
    plt.xticks(x_coordinates, y)
    plt.show()

with open('C:/Users/Lenovo/Desktop/PYTHON/HW5/years.txt', 'w+') as years_doc:
    for element in top_250_movies:
        year = element[:-1]
        years_doc.write(year + '\n')

    dct2 = {}
    for year in years_doc:
        dct2[year] = dct2.get(year, 0) + 1

num2 = Counter(dct2)
x2 = list(num2.values())
y2 = list(num2.keys())
x_coordinates2 = np.arange(len(num2.keys()))
plt.bar(x_coordinates2, x2)
plt.xticks(x_coordinates2, y2)
plt.show()
