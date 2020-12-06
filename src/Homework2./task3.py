"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все
пробелы. Например, если было введено "abc cde def", то должно быть
выведено "abcdef".
"""
str_ = 'abc cde def'
new_str = ''
for letter in str_:
    if letter not in new_str and letter != ' ':
        new_str += letter
print(new_str)
