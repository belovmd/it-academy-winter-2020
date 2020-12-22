""" Найти самое длинное слово в введенном предложении.
    Учтите что в предложении есть знаки препинания.
"""


import string


str_ = 'Хлопотное, дельце!!!!!'
longest_word = ''

for i in string.punctuation:
    str_ = str_.replace(i, '')
new_str = str_.split()

for words in new_str:
    if len(words) > len(longest_word):
        longest_word = words

print('Самое длиное слово:', longest_word)
