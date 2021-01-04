"""Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте."""
str_ = input()
clear_str = ""
symb = ",.;"

for el in str_:
    if el not in symb:
        clear_str += el

dct = {}
for el in clear_str.split():
    dct[el] = dct.get(el, 0) + 1

counter = 0
for el in dct:
    counter += 1
print(counter)
