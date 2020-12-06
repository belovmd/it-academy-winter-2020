import string


""" 
    Task 2. Найти самое длинное слово в введенном предложении.

    Учтите что в предложении есть знаки препинания.
    Выводит первое найденное самое длинное слово
"""


str_ = ("The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to " 
        "using 'Content here, content here', making it look like readable English.")
prepared_str = ""
longest_word = ""

for sub_str in str_:
    for symbol in sub_str:
        if symbol in string.punctuation:
            prepared_str += " "
        else:
            prepared_str += symbol

for word in prepared_str.split(" "):
    if len(word) > len(longest_word):
        longest_word = word

print(f"Самое длинное слово в предложении - {longest_word}")
