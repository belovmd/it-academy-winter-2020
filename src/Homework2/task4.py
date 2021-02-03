"""Посчитать количество строчных (маленьких) и
   прописных (больших) букв в введенной строке.
   Учитывать только английские буквы.
"""


my_string = input()
small_letters = 0
big_letters = 0

for i in my_string:
    if "a" <= i <= "z":
        small_letters += 1
    elif "A" <= i <= "Z":
        big_letters += 1
    else:
        pass
print("Строчных", small_letters, "и",
      "прописных", big_letters, "букв.")
