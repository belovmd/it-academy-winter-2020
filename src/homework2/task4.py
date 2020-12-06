import string


""" 
    Task 4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

    Учитывать только английские буквы.
"""


str_ = "1914 translation by H. Rackham"
lowers, uppers = 0, 0

for letter in str_:
    if letter in string.ascii_lowercase:
        lowers += 1
    elif letter in string.ascii_uppercase:
        uppers += 1

print(f"Количество строчных букв: {lowers}, количество пописных букв: {uppers}")

