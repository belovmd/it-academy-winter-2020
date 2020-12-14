"""Вводится строка. Требуется удалить из нее
   повторяющиеся символы и все пробелы"""


text = "dfvu oewuc 11!!=  iowcm?"
SYMB_TO_REPLACE = ',?.;:{)}[!= '
result_string = ""
for element in text:
    if element not in SYMB_TO_REPLACE and element not in result_string:
        result_string += element

print(result_string)
