import re


class Movie:
    def __init__(self, distribution, votes, rank, title, year):
        self.distribution = distribution
        self.rank = rank
        self.votes = votes
        self.title = title
        self.year = year


def extract_from_file(strings_list):
    movies_data = []
    for string in strings_list:
        if len(movies_data) == 250:
            break

        if re.match(r'^ {6}[0-9.]{10}', string):
            movies_data.append(string)

    return __build_movies_from_string(movies_data)


def __build_movies_from_string(movies_data_list):
    movies = []
    for movie_string in movies_data_list:
        year = re.search(r'\([0-9]{4}(/(I|II|III|IV))?\)',
                         movie_string.strip()).group(0)

        movies_args = re.split(r' {2,}',
                               movie_string.strip().replace(year, ''))

        movies.append(Movie(*movies_args, year[1:-1]))
    return movies
