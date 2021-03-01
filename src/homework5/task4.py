# В файле хранятся данные с сайта IMDB. Скопированные
# данные хранятся в файле ./data_hw5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо
# вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt –
# названия файлов, ratings.txt – гистограмма рейтингов,
# years.txt – гистограмма годов.
import matplotlib.pyplot as plt
import re

ratings = []
titles = []
years = []

# Открытие, прочтение и ран возможной ошибки
try:
    with open('ratings.list') as file:
        print('Файл прочитан!')
except FileNotFoundError:
    print('Файл не обнаружен!')
finally:
    pass

fh = open('ratings.list', encoding="ISO-8859-1")
all_lines = fh.readlines()

# Создание файла top250_movies.txt и списков данных
for line in all_lines[28:278]:
    list_line = line.split()
    years.extend(re.findall(r'(\d+)', str(list_line[-1])))
    num, num2, rating, *title = list_line
    str_line = ''
    ratings.append(rating)
    with open('top250_movies', 'a') as file:
        for el in title:
            # Другого способа распаковки найти не получилось
            str_line += f'{el} '
        titles.append(str_line)
        file.writelines(f'{str_line}\n')
print('Файл "top250_movies" создан!')


# Создание ratings.txt
x = sorted(set(ratings))
ratings_for_histogram = []

for el in x:
    ratings_for_histogram.append(ratings.count(el))

y = ratings_for_histogram
plt.bar(x, y, label='Рейтинг')
plt.xlabel('Рейтинг')
plt.ylabel('Количество фильмов в топ-250')
plt.title('Гистограмма рейтингов')
plt.savefig('ratings')
plt.show()

with open('ratings.txt', 'a') as file_ratings:
    for el in ratings:
        file_ratings.writelines(f'{el}\n')
print('Файл "ratings.txt" создан!')


# Создание years.txt
x = sorted(set(years))
years_for_histogram = []

for el in x:
    years_for_histogram.append(years.count(el))

y = years_for_histogram
plt.figure(figsize=(15,5))
plt.tick_params(axis='x', which='major', labelsize=6)
plt.tight_layout()
plt.xticks(
    rotation=90
)
plt.bar(x, y, label='Год')
plt.xlabel('Год')
plt.ylabel('Количество фильмов в топ-250')
plt.title('Гистограмма годов')
plt.savefig('years')
plt.show()

with open('years', 'a') as file_years:
    for el in years:
        file_years.writelines(f'{el}\n')
print('Файл "years.txt" создан!')
