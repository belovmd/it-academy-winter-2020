"""Введите строку. Удалите из нее
   повторяющиеся символы и все пробелы
"""


str = input('Please enter your string:')
result = ''
for i in str:
    if (i not in result) and (i != ' '):
        result += i
print(result)
