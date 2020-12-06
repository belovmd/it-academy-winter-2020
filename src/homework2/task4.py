"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв
в введенной строке. Учитывать только английские буквы.
"""

my_string = input('Введите  строку на английском языке: ')
upper_case = 0
lower_case = 0
index = 0
for char in my_string:
    if 'a' <= char[index] <= 'z':
        lower_case += 1
    elif 'A' <= char[index] <= 'Z':
        upper_case += 1
print('Количество строчных букв: ' + str(lower_case))
print('Количество прописных букв: ' + str(upper_case))
