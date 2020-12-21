# 4. Посчитать количество строчных (маленьких) и прописных (больших) букв
# в введенной строке. Учитывать только английские буквы.
str_ = 'aBCcDdedEfF'
num_small = 0
num_big = 0

for letter in str_:
    if 'a' <= letter <= 'z':
        num_small += 1
    else:
        if 'A' <= letter <= 'Z':
            num_big += 1

print("Прописных букв в строке: " + str(num_big))
print("Строчных букв в строке: " + str(num_small))
