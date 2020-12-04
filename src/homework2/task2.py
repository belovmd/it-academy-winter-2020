"""Найти самое длинное слово в введенном предложении.
    Учтите что в предложении есть знаки препинания.
"""


my_string = 'this is a good sentence but not the best one'
new_string = my_string.split()
longest_word = ''

for words in new_string:
    if len(words) > len(longest_word):
        longest_word = words

print(longest_word)
