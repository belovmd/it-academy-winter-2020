# 6. Определите, является ли число палиндромом.


str_ = input()
str_ = str_.replace(' ', '').lower()
if str_ == str_[::-1]:
    print('Palindrom')
else:
    print('Not palindrom')
