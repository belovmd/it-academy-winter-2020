"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
   введенной строке. Учитывать только английские буквы.
"""

string = input('Enter string: ')
low_number = 0
up_number = 0
for i in string:
    if 'a' <= i <= 'z':
        low_number += 1
    elif 'A' <= i <= 'Z':
        up_number += 1
    else:
        pass
print(low_number)
print(up_number)
