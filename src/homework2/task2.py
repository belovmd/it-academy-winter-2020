# 2. Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
import string

predl = 'Найти самое... длинное {слово, в <введенном: предложении.'
result = ''

for znak in string.punctuation:
    predl = predl.replace(znak, "")

for word in predl.split():
    if len(word) > len(result):
        result = word
print('Самое длинное слово в предложении: ' + result)
