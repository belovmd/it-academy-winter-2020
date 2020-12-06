"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все
пробелы. Например, если было введено "abc cde def", то должно быть
выведено "abcdef".
"""
text = 'abc cde def'
txt = ''
for new_text in text:
    if new_text not in txt and new_text != ' ':
        txt += new_text
print(txt)
