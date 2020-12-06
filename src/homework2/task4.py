"""Посчитать количество строчных (маленьких) и прописных (больших)
   букв в введенной строке. Учитывать только английские буквы
"""

sentence = input('Please enter your sentence:')
letter = 0
LETTER = 0
for i in sentence:
    if 'a' <= i <= 'z':
        letter += 1
    elif 'A' <= i <= 'Z':
        LETTER += 1
    else:
        pass
print(letter)
print(LETTER)
