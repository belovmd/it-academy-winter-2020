"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
"""
import string
my_string = ('…занудная регулярность при выполнении совсем неинтересных действий может привести к очень хорошему'
             ' результату.')
TO_REPLACE = string.punctuation
new_string = ''
for char in my_string:
    if char not in TO_REPLACE:
        new_string += char

my_list = new_string.split()
the_longest_word = ''

for element in my_list:
    if len(element) > len(the_longest_word):
        the_longest_word = element
    else:
        pass
print(the_longest_word)
