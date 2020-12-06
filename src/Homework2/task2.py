"""2. Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания.
"""


str_ = input('Введите текст: ')
new_str = str_.split()
long_word = ''
for words in new_str:
    if len(words) > len(long_word):
        long_word = words
print(long_word)
