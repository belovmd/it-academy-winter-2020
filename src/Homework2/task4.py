""" Посчитать количество строчных (маленьких) и
    прописных (больших) букв в введенной строке.
    Учитывать только английские буквы"""


str_ = 'jjdfhvbUnj  hjsdinUUh  kKKJJBDNM'
big_letters = 0
small_letters = 0

for element in str_:
    if 'a' <= element <= 'z':
        small_letters += 1
    if 'A' <= element <= 'Z':
        big_letters += 1

print('Прописных букв в предложении:', big_letters)
print('Строчных букв в предложении:', small_letters)
