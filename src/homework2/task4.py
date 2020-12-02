"""
 Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
 Учитывать только английские буквы.
"""
my_str = 'HERE IS A SMALL FACT You are going to die'
l_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l_count = 0
s_letters = 'abcdefghijklmnopqrstuvwxyz'
s_count = 0
for symbol in my_str:
    if symbol in l_letters:
        l_count += 1
    elif symbol in s_letters:
        s_count += 1
    else:
        pass
print('Количество больших букв в строке:', l_count)
print('Количество маленьких букв в строке:', s_count)
