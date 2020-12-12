"""Найти самое длинное слово в введенном предложении.
    Учтите что в предложении есть знаки препинания.
"""

import string


my_string = 'this is a good sentence, but not the best one.'
to_split = string.punctuation
new_string = ''

for char in my_string:
    if char not in to_split:
        new_string += char

final_string = new_string.split()
longest_word = ''

for words in final_string:
    if len(words) > len(longest_word):
        longest_word = words

print(longest_word)
