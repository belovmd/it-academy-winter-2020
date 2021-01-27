import re


# класс фильм, берем все свойства, которые можем из файла
class Movie:
    def __init__(self, distribution, votes, rank, title, year):
        self.distribution = distribution
        self.rank = rank
        self.votes = votes
        self.title = title
        self.year = year


# обходим строки файла
def extract_from_file(strings_list):
    # Массив, куда мы будем записывать нужные нам строки, отсеивая объяснения
    movies_data = []
    for string in strings_list:
        # Если уже записали топ250, ты выходим из цикла
        if len(movies_data) == 250:
            break
        # re-модуль для работы с регулярными выражениями, позволяют находить
        # в строках определённые паттерны,например тут,символ ^ -начало строки
        # "пробел"{6} означает, в начале строки должны быть 6 пробелов,
        # [0-9.]{10} означает, что следующими
        # символами должны быть цифры либо точка, их должно быть 10
        # если такие сходства найдены, то записываем такую строку в массив
        if re.match(r'^ {6}[0-9.]{10}', string):
            movies_data.append(string)
        # к концу выполнения этой функции у нас есть массив строк(movies_data):
        # [.., '.. 8.9  The Lord of ..: The Return of the King (2003)', ..]
        # мы должны её преобразовать, чтобы было удобно использовать при помощи:
    return __build_movies_from_string__(movies_data)


def __build_movies_from_string__(movies_data_list):
    # массив, куда будем записывать экземпляры класса Movie
    movies = []
    for movie_string in movies_data_list:
        # ищем по паттерну года "(2015)" и записываем в переменную, по тому же принципу
        # иногда попадаются года подобного плана (2017\I) (2014\II), поэтому мы должны добавить в паттерн
        # конструкцию (I|II|III|IV))?  - в скобках группируем символы, может быть один из тех, что
        # написаны между | , а знак вопроса означает, что эта вся группа может быть, а может и не быть
        # -
        # метод group(0) возвращает саму найденую с помощью регулярки строку.
        year = re.search(r'\([0-9]{4}(/(I|II|III|IV))?\)', movie_string.strip()).group(0)
        # replace заменяет строку с годом на пустую(другими словами, вырезаем год и строки, потому что
        # уже записали его в переменную year)
        # разбиваем строку на массив отдельных строк со значениями Votes, Rank и тд
        movies_args = re.split(r' {2,}', movie_string.strip().replace(year, ''))
        # создаем экземпляр класса, в качестве аргументов берём разбитую на строки movies_args
        # year[1:-1] означает, что мы  из строки "(2015)" вырезаем первый и последний символ, чтобы получить "2015"
        movies.append(Movie(*movies_args, year[1:-1]))
    return movies
