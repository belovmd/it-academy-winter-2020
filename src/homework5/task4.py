""" В файле хранятся данные с сайта IMDB.
    a.Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
    b.Найдите ТОП250 фильмов и извлеките заголовки.
    c.Программа создает 3 файла  top250_movies.txt – названия файлов,
    ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""


movies_num = 250
read_line = 28
read_to = read_line + movies_num
year_ = 5
rating_offset = 0.6


def save_titles(movies, file_name):
    if not movies:
        return

    with open(file_name, 'w', encoding='utf8') as file:
        for line in movies:
            file.write(f"{line}\n")


def save_years(movies, file_name):
    if not movies:
        return

    min_year = int(min(values.get('year_') for values in movies.values()))
    start_year = min_year - year_

    with open(file_name, 'w') as file:
        for line in movies.values():
            year = int(line.get('year_'))
            year_with_offset = year - start_year
            file.write(f"{year_with_offset * '+'} {year}\n")


def save_ratings(movies, file_name):
    if not movies:
        return

    min_rating = float(min(values.get('rating') for values in movies.values()))
    start_rating = min_rating - rating_offset

    with open(file_name, 'w', encoding='utf-8') as file:
        for line in movies.values():
            rating = float(line.get('rating'))
            rating_with_offset = int((rating * 10) - (start_rating * 10))
            file.write(f"{rating_with_offset * '+'} {rating}\n")


def reader_to_safe():

    movies = dict()

    folder = "lists/"
    top_movies_file_name = folder + "top250_movies.txt"
    ratings_file_name = folder + "ratings.txt"
    years_file_name = folder + "years.txt"

    try:
        with open(f'{folder}ratings.list', 'r', encoding="ISO-8859-1") as fl:
            for line in fl.readlines()[read_line:read_to]:
                [distribution, votes, rank, *title, year] = line.split()
                movies[" ".join(title)] = {"rating": rank, "year_": year[1:5]}

    except FileNotFoundError as err:
        print(err)
    else:
        save_titles(movies, top_movies_file_name)
        save_ratings(movies, ratings_file_name)
        save_years(movies, years_file_name)


reader_to_safe()
