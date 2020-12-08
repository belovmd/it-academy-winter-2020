"""Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания.  НЕ СДЕЛАНО !!!!
"""


my_string = input()
w_list = my_string.split()
c = 0
for i in range(len(w_list)):
    if len(w_list[i]) > c:
        c = len (w_list[i])
        word = w_list[i]
print(word)