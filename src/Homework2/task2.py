"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""
import re

sentence = input('введите предложение: ')
def longest_word(sentence):
    words = re.sub('[^\w ]', '', sentence).split(' ')
    return max(words, key=len)
longest = longest_word(sentence)
print(f'Самое длинное слово - "{longest}". {len(longest)} символов.')
