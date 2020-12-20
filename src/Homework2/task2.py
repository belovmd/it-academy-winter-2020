import string
"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""


text = input('введите предложение: ')
e = string.punctuation + '—'
for i in range(len(e)):
    text = text.replace(e[i], "")
list_ = text.split()

word_ = ''
len_ = 0

for word in list_:
    if len(word) > len_:
        word_ = word
        len_ = len(word)

print('Самое длинное слово - ' + word_, end='\n' + str(len_) + ' - символов')
