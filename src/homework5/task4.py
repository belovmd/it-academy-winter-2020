"""В файле хранятся данные с сайта IMDB.
   Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
   Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
   Найдите ТОП250 фильмов и извлеките заголовки.
   Программа создает 3 файла  top250_movies.txt – названия файлов,
   ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
   Задачу поместите в файл task4.py в папке src/homework5.
"""

from homework5 import movies
from homework5 import histogram
from homework5 import file_utils


# Передаем в функцию массив объектов, получаем на выходе
# массив со значениями определённого свойства(prop) этих объектов
def __map_to_property__(obj, prop):
    return list(map(lambda movie: getattr(movie, prop), obj))


file_to_open = './data_hw5/ratings.list'
file_to_write_titles = 'top250_movies.txt'
file_to_write_years_his = 'years.txt'
file_to_write_ratings_histogram = 'ratings.txt'
file_lines = file_utils.try_to_read(file_to_open)

movies_list = movies.extract_from_file(file_lines)
titles_list = __map_to_property__(movies_list, 'title')
movies_titles = '\n'.join(titles_list)
# выводим названия фильмов
print(movies_titles)

# пишем названия фильмов в файл
file_utils.try_to_write(file_to_write_titles, movies_titles)

# строим и записываем гистограмму рейтинга
rank_list = __map_to_property__(movies_list, 'rank')
rating_histogram = histogram.build(rank_list, titles_list)
file_utils.try_to_write(file_to_write_ratings_histogram, rating_histogram)

# строим и записываем годовую гистограмму
year_his_label_length = 6
movies_sorted_by_year = sorted(movies_list, key=lambda movie: movie.year)
years_list = __map_to_property__(movies_sorted_by_year, 'year')
rank_list = __map_to_property__(movies_sorted_by_year, 'rank')
year_his = histogram.build(rank_list, years_list, year_his_label_length)
file_utils.try_to_write(file_to_write_years_his, year_his)
