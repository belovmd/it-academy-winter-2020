"""Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания.
"""

string = input('Введите предложение: ')
long_word = max(string.split(), key=len)
print(f'Самое длинное слово в предложении:{long_word}')
