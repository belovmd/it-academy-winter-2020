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


def save_titles(movies, file_name):
    """Запись названия фильмов в файл

    :param movies: dict. Содержит информацию о фильмах
    :param file_name: str. путь к файлу
    :return: None
    """
    if not movies:
        return

    with open(file_name, 'w') as file:
        for line in movies:
            file.write(f"{line}\n")


def save_years(movies, file_name):
    """Записать информации о рейтингах фильмов в файл в виде гистограммы

    :param movies: dict. Содержит информацию о фильмах
    :param file_name: str. путь к файлу для записи
    :return: None
    """
    if not movies:
        return

    min_year = int(min(values.get('year') for values in movies.values()))
    offset = 5
    start_year = min_year - offset

    with open(file_name, 'w') as file:
        for line in movies.values():
            year = int(line.get('year'))
            year_with_offset = year - start_year
            file.write(f"{year_with_offset * '+'} {year}\n")


def save_ratings(movies, file_name):
    """Записать информации о годах фильмов в файл в виде гистограммы

    :param movies: dict. Содержит информацию о фильмах
    :param file_name: str. путь к файлу
    :return: None
    """
    if not movies:
        return

    min_rating = float(min(values.get('rating') for values in movies.values()))
    offset = 0.6
    start_rating = min_rating - offset

    with open(file_name, 'w') as file:
        for line in movies.values():
            rating = float(line.get('rating'))
            rating_with_offset = int((rating * 10) - (start_rating * 10))
            file.write(f"{rating_with_offset * '+'} {rating}\n")


def reader_to_safe():
    """Чтение файла с информацией о фильмах для дальнейшего сохранения

    отдельной информации или построения гистограммы на ее основании

    :return: None
    """

    numbers_of_movies = 250
    movies = dict()

    folder = "movies/"
    top_movies_file_name = folder + "top250_movies.txt"
    ratings_file_name = folder + "ratings.txt"
    years_file_name = folder + "years.txt"

    try:
        read_from = 28
        read_to = read_from + numbers_of_movies

        with open(f'{folder}ratings.list', 'r', encoding="ISO-8859-1") as fl:
            for line in fl.readlines()[read_from:read_to]:
                [distribution, votes, rank, *title, year] = line.split()
                movies[" ".join(title)] = {"rating": rank, "year": year[1:5]}

    except FileNotFoundError as err:
        print(err)
    else:
        save_titles(movies, top_movies_file_name)
        save_ratings(movies, ratings_file_name)
        save_years(movies, years_file_name)


reader_to_safe()
