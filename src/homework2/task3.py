""" Вводится строка. Требуется удалить из
    нее повторяющиеся символы и все пробелы.
    Например, если было введено "abc cde def",
    то должно быть выведено "abcdef".
"""


str_ = "abc cde def"
new_str = ''
for symbol in str_:
    if symbol not in new_str and symbol != ' ':
        new_str += symbol
print(new_str)
