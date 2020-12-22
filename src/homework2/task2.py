"""Найти самое длинное слово в введенном предложении
   Учтите, что в предложении есть знаки препинания
"""


import string

str_ = input('Please enter a sentence:')
add_str = ""

for symbol in str_:
    if symbol in string.punctuation:
        add_str += " "
    else:
        add_str += symbol

print(max(add_str.split(), key=len))
