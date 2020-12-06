"""3.Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
   Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""


str_ = "abc cde def"
newSTR = ''
for symbol in str_:
    if symbol not in newSTR and symbol != ' ':
        newSTR += symbol
print(newSTR)
