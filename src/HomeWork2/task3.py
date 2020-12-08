# 3. Вводится строка. Требуется удалить из нее повторяющиеся
# символы и все пробелы. Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".
str_ = 'abc cde def'
concatenation = ''
result = ''

for letter in str_:
    if letter != ' ':
        concatenation += letter

for letter2 in concatenation:
    if letter2 not in result:
        result += letter2

print(result)
