""" Найти самое длинное слово в введенном предложении.
    Учтите что в предложении есть знаки препинания.
"""


str_ = input('Введите предложение: ')
new_str = str_.split()
longest_word = ''

for words in new_str:
    if len(words) > len(longest_word):
        longest_word = words

print('Самое длиное слово:', longest_word)

