'''
Посчитать количество строчных (маленьких)
и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
'''
word = input(': ')
small_letter = 0
big_letter = 0
for letter in word:
    if 'a' <= letter <= 'z':
        small_letter += 1
    elif 'A' <= letter <= 'Z':
        big_letter += 1
    else:
        pass
print(big_letter, small_letter)
