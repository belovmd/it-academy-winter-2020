"""
 Посчитать количество строчных (маленьких) и
 прописных (больших) букв в введенной строке.
 Учитывать только английские буквы.
"""
# я не совсем поняла, что с islower()
my_str = 'HERE IS A SMALL FACT You are going to die'
s_count = 0
l_count = 0

for symbol in my_str:
    if 'a' <= symbol <= 'z':
        s_count += 1
    elif 'A' <= symbol <= 'Z':
        l_count += 1

print('Количество больших букв в строке:', l_count)
print('Количество маленьких букв в строке:', s_count)
