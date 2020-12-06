"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания."""

str_ = input("Введите предложение: ")
str_ = str_.replace(",", "")
str_ = str_.strip(".")
str_ = str_.split()
count = 0
for word in str_:
    if len(word) > count:
        count = len(word)
        max_word = word
print("Самое длинное влово -", word)

