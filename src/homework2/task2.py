import string

"""Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания.
"""

in_str = input('Введите предложение:')
element = string.punctuation
for i in range(len(element)):
    in_str = in_str.replace(element[i], "")

long_word = max(in_str.split(), key=len)
print(f'Самое длинное слово в предложении:{long_word}')
