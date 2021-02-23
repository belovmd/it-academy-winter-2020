"""В файле хранятся данные с сайта IMDB. Скопированные
   данные хранятся в файле ./data_hw5/ ratings.list.
   Откройте и прочитайте файл(если его нет необходимо
   вывести ошибку).
   Найдите ТОП250 фильмов и извлеките заголовки.
   Программа создает 3 файла  top250_movies.txt – названия
   файлов, ratings.txt – гистограмма рейтингов, years.txt –
   гистограмма годов.
"""


import matplotlib.pyplot as plt


try:
    file = open('ratings.list', 'r')
    lines = file.readlines()
    list_headers = lines[28:278]
except Exception as error_text:
    print(error_text)


# Функция для записи данных в файл
def write_titles_to_file(titles):
    titles_txt = open(name_file, 'w', encoding='UTF-8')
    titles_txt.writelines(titles)
    titles_txt.close()


# топ-250
list_titles = []
for list_elem in list_headers:
    name_title = ' '.join(list_elem.split()[3:])
    list_titles.append(name_title)
titles_str = '\n'.join(list_titles)
name_file = 'top250_movies.txt'
write_titles_to_file(titles_str)

# рейтинги
list_ratings = []
for list_elem in list_headers:
    name_rating = ' '.join(list_elem.split()[2::20])
    list_ratings.append(name_rating)
ratings_str = '\n'.join(list_ratings)
name_file = 'ratings.txt'
write_titles_to_file(ratings_str)

# количество фильмов с одним рейтингом для гистрограммы
dict_ratings = {i: list_ratings.count(i) for i in set(list_ratings)}
plt.bar(list(dict_ratings.keys()), dict_ratings.values(), color='g')
plt.tick_params(axis='x', labelsize=6, rotation=90)
plt.show()

# годы
list_years = []
for list_elem in list_headers:
    name_year = ' '.join(list_elem.split()[-1::20])
    list_years.append(name_year[1:5])
years_str = '\n'.join(list_years)
name_file = 'years.txt'
write_titles_to_file(years_str)

# количество фильмов одного года выпуска для гистрограммы
dict_years = {j: list_years.count(j) for j in set(list_years)}
plt.bar(list(dict_years.keys()), dict_years.values(), color='g')
plt.tick_params(axis='x', labelsize=4, rotation=90)
plt.show()
