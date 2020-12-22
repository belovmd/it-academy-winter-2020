"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""
import string
my_string = input(': ')
longest_word = ''
for ch in string.punctuation:
    my_string = my_string.replace(ch, '')
new_str = my_string.split()
for word in new_str:
    if len(longest_word) < len(word):
        longest_word = word
print(longest_word)
