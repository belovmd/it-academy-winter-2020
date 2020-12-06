'''
Посчитать количество строчных (маленьких) и
прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
'''
word = input('Enter text: ')
small = 0
big = 0
for word_1 in word:
    if 'a' <= word_1 <= 'z':
        small += 1
    elif 'A' <= word_1 <= 'Z':
        big += 1
    else:
        pass
print('больших букв-' + str(big))
print('маленьких букв-' + str(small))
