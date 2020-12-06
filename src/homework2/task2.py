import string

"""
2. Найти самое длинное слово в введенном предложении. 
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""

my_string = "Time Out выбрал 8 самых интересных сериалов осени — "\
            "среди них новый проект итальянца Луки Гуаданьино, " \
            "конспирологический триллер с Джудом Лоу, сай-фай "\
            "драма от Netflix, а также хоррор-комедия при участии " \
            "легендарного дуэта Ника Фроста и Саймона Пегга."
print(my_string)
e = string.punctuation + '—'
for i in range(len(e)):
    my_string = my_string.replace(e[i], "")
my_list = my_string.split()

longest_word = ''
max_len = 0

for word in my_list:
    if len(word) > max_len:
        longest_word = word
        max_len = len(word)
print('Самое длинное слово в предложении -  ' + longest_word)