"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""
str_ = 'abc cde def'
new_str = ''
TO_REPLACE = ' '
for char in str_:
    if char not in new_str:
        if char not in TO_REPLACE:
            new_str += char
final_str = ''.join(new_str)
print(final_str)
