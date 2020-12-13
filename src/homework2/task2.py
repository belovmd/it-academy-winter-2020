"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания."""

import string

str_ = input("Введите предложение: ")
str_new = ""

for el in str_:
    if el not in string.punctuation:
        str_new += el

str_new = str_new.split()

count = 0
for word in str_new:
    if len(word) > count:
        count = len(word)
        max_word = word

print("Самое длинное влово -", max_word)
