"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

# через сплит
str_ = 'abc cde def'
new_str = ''
for char in str_:
    if char not in new_str:
        new_str += char

lst = new_str.split()
final_str = ''.join(lst)
print(final_str)
