"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""
my_string = input(': ').split()
int_ = 0
for char in my_string:
    if len(char) > int_:
        int_ = len(char)
        word = char
print('Самое длинное слово :', word)
