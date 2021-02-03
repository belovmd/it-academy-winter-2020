"""В файле хранятся данные с сайта IMDB. Скопированные
   данные хранятся в файле ./data_hw5/ ratings.list.
   Откройте и прочитайте файл(если его нет необходимо
   вывести ошибку).
   Найдите ТОП250 фильмов и извлеките заголовки.
   Программа создает 3 файла  top250_movies.txt – названия
   файлов, ratings.txt – гистограмма рейтингов, years.txt –
   гистограмма годов.
"""


def write_titles_to_file(titles):
    titles_txt = open('top250_movies.txt', 'w', encoding='UTF-8')
    titles_txt.writelines(titles)
    titles_txt.close()


try:
    file = open('ratings.list', 'r')
    lines = file.readlines()
    list_headers = lines[28:279]
    list_titles = []
    for list_elem in list_headers:
        name_title = ' '.join(list_elem.split()[3:])
        list_titles.append(name_title)
    titles_str = '\n'.join(list_titles)
    write_titles_to_file(titles_str)

except Exception as error_text:
    print(error_text)
