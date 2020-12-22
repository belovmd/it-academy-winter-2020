"""Посчитать количество строчных (маленьких) и прописных (больших)
   букв в введенной строке. Учитывать только английские буквы
"""

sentence = input('Please enter your sentence:')
lowers = 0
uppers = 0
for i in sentence:
    if 'a' <= i <= 'z':
        lowers += 1
    elif 'A' <= i <= 'Z':
        uppers += 1
    else:
        pass
print(lowers)
print(uppers)
