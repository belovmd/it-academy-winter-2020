"""Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания"""


text = "какое морозное, свежее утро."
SYMB_TO_DELETE = ',.'
result_str = ''
for element in text:
    if element not in SYMB_TO_DELETE:
        result_str += element
for element in result_str.split():
    print()
print('Самое длинное слово:', max(result_str.split(' '), key=len))
