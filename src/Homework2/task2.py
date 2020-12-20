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

longest_word = ''
max_len = 0

for word in list_:
    if len(word) > max_len:
        longest_word = word
        max_len = len(word)

print('Самое длинное слово - ' + longest_word + ' ', end='\n' + str(max_len) + ' - символов')
