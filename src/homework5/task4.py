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
    num, rating, num3, *title = list_line
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
x = [x for x in range(1, 251)]
y = [int(y) for y in ratings]
plt.bar(x, y, label='Рейтинг')
plt.xlabel('Позиция в "TOP 250"')
plt.ylabel('Рейтинг')
plt.title('Гистограмма рейтингов')
plt.savefig('ratings')
plt.show()

with open('ratings.txt', 'a') as file_ratings:
    for el in ratings:
        file_ratings.writelines(f'{el}\n')
print('Файл "ratings.txt" создан!')


# Создание years.txt
x = [x for x in range(1, 251)]
y = [int(y) for y in years]
plt.bar(x, y, label='Год')
plt.xlabel('Позиция в "TOP 250"')
plt.ylabel('Год')
plt.title('Гистограмма годов')
plt.savefig('years')
plt.show()

with open('years', 'a') as file_years:
    for el in years:
        file_years.writelines(f'{el}\n')
print('Файл "years.txt" создан!')
