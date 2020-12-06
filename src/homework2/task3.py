"""
    Task 3. Вводится строка.
    Требуется удалить из нее повторяющиеся символыи все пробелы.
"""


str_ = "abc cde def"
unique_str = ""

for substring in str_:
    if substring == " " or substring in unique_str:
        continue
    else:
        unique_str += substring

print(unique_str)
