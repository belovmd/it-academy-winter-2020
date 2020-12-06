""" Посчитать количество строчных (маленьких) и
    прописных (больших) букв в введенной строке.
    Учитывать только английские буквы.
"""


str_ = 'SGHJHgHJGhjgJHgJHGHJJHGJHghjdsadsadasdas'
lowercase_letter = 0
uppercase_letter = 0
for i in str_:
    if 'A' <= i <= 'Z':
        uppercase_letter += 1
    elif 'a' <= i <= 'z':
        lowercase_letter += 1
    else:
        pass
print(uppercase_letter)
print(lowercase_letter)
