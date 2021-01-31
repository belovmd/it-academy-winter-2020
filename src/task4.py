import matplotlib.pyplot as plt
import pandas as pd


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
    """Запись информации о годах, в которые были сняты фильмы,

    в файл для возможности построения гистограммы

    :param movies: dict. Содержит информацию о фильмах
    :param file_name: str. путь к файлу
    :return: None
    """
    if not movies:
        return

    min_year = min(int(items['year']) for items in movies.values())
    offset = 5
    start_year = min_year - offset

    with open(file_name, 'w') as file:
        file.write("Position, Year, Year to view, Offset\n")

        for i, line in enumerate(movies.values()):
            year = line.get('year')
            year_to_view = int(year) - start_year
            file.write(f"{i+1}, {year}, {year_to_view}, {start_year}\n")


def save_ratings(movies, file_name):
    """Запись информации о рейтингах фильмов для возможности построения

    гистограммы

    :param movies: dict. Содержит информацию о фильмах
    :param file_name: str. путь к файлу
    :return: None
    """
    if not movies:
        return

    min_rating = min(float(items['rating']) for items in movies.values())
    offset = 0.1
    start_rating = float(min_rating) - offset

    with open(file_name, 'w') as file:
        file.write("Position, Rating, Rating to view, Offset\n")

        for i, line in enumerate(movies.values()):
            rating = float(line.get('rating'))
            rating_to_view = (int(rating * 10) - (start_rating * 10)) / 10
            file.write(f"{i + 1}, {rating}, "
                       f"{rating_to_view}, {start_rating}\n"
                       )


def show_bar_chart(file_name, label):
    """Построение гистограммы на основании чтения файла

    :param file_name: str. Путь к файлу
    :param label: str. Лейбл для названия полей
    :return: None
    """
    # read file
    df = pd.read_csv(
        file_name,
        names=['position', 'field', 'fieldToView', 'start_charts'],
        skiprows=1
    )

    # prepare chart
    plt.bar(
        df.position,
        df.fieldToView,
        color='purple',
        bottom=df.start_charts
    )

    # set figure window title
    plt.gcf().canvas.set_window_title(file_name)

    # set label to left side of chart
    plt.ylabel(label)

    # show chart
    plt.show()


def reader_to_safe():
    """Чтение файла с информацией о фильмах для дальнейшего сохранения

    информации и построения гистограммы

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
        show_bar_chart(ratings_file_name, 'ratings')

        save_years(movies, years_file_name)
        show_bar_chart(years_file_name, 'years')


reader_to_safe()
