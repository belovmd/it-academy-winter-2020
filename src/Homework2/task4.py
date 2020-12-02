""" Посчитать количество строчных (маленьких) и
    прописных (больших) букв в введенной строке.
    Учитывать только английские буквы"""

str_ = 'jjdfhvbUnj  hjsdinUUh  kKKJJBDNM'
len_MAJ = 0
len_small = 0
for element in str_:
    if 'a' <= element <= 'z':
        len_small += 1
    if 'A' <= element <= 'Z':
        len_MAJ += 1
print('Прописных букв в предложении:', len_MAJ)
print('Строчных букв в предложении:', len_small)
