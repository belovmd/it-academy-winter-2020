"""Найти самое длинное слово в введенном предложении
   Учтите, что в предложении есть знаки препинания
"""


s = input('Please enter a sentence:')
print(max(s.split(), key=len))
