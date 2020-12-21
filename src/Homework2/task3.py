""" Вводится строка.
    Требуется удалить из нее повторяющиеся символы и все пробелы.
"""


my_string = input()
string_w_spaces = ''.join(my_string.split())
new_string = ""

for i in string_w_spaces:
    if i not in new_string:
        new_string += i
print(new_string)


