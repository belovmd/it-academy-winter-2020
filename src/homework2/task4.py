"""Посчитать количество строчных (маленьких) и прописных (больших) букв
    в введенной строке. Учитывать только английские буквы.
"""


str_ = 'BIG LETTERS, small letters'
str_ = ' '.join(str_).split()
low_number = 0
up_number = 0

for letter in str_:
    if 'a' <= letter <= 'z':
        low_number += 1
    elif 'A' <= letter <= 'Z':
        up_number += 1

print(low_number, up_number)
