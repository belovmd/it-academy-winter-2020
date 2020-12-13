"""Вводится строка. Требуется удалить из нее
повторяющиеся символы и все пробелы."""

str_ = input("Введите строку: ")
str_ = " ".join(str_).split()
result_string = []
for element in str_:
    if element not in result_string:
        result_string.append(element)
print("".join(result_string))
