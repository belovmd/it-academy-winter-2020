"""4. Посчитать количество строчных (маленьких) и прописных (больших)
   букв в введенной строке. Учитывать только английские буквы.
"""


text = input()
small_let = 0
large_let = 0
for symbol in text:
    if 'a' <= symbol <= 'z':
        small_let += 1
    elif 'A' <= symbol <= 'Z':
        large_let += 1
print('Small letters', small_let)
print('Large letters', large_let)
