"""Вводится строка. Требуется удалить из нее
повторяющиеся символы и все пробелы."""

str_ = input("Введите строку: ")
symbols = ".,/!| "
result_string = ""
for element in str_:
    if element not in symbols:
        result_string += element
print(result_string)
