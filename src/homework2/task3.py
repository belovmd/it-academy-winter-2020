"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""
my_string = 'abc cde def'
new_string = ''
for char in my_string:
    if not char == ' ':
        if char not in new_string:
            new_string = new_string + char
print(new_string)
