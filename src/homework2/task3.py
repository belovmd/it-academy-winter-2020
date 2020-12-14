"""
    Task 3. Вводится строка.
    Требуется удалить из нее повторяющиеся символыи все пробелы.
"""


str_ = "abc cde def"
unique_str = ""

for symbol in str_:
    if symbol == " " or symbol in unique_str:
        continue
    else:
        unique_str += symbol

print(unique_str)
