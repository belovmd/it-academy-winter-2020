"""Вводится строка. Требуется удалить из нее повторяющиеся символы и пробелы.
    Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


str_ = 'abc cde def'
str_ = ' '.join(str_).split()
new_str_ = []

for char in str_:
    if char not in new_str_:
        new_str_.append(char)

print(''.join(new_str_))
