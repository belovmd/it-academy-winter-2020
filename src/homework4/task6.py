import re
import string


"""
    Task 6. Слова.

    Во входной строке записан текст. Словом считается последовательность
    непробельных символов идущих подряд, слова разделены одним или большим
    числом пробелов или символами конца строки.
    Определите, сколько различных слов содержится в этом тексте.
"""


words = []
for word in input("Текст: ").split():
    words += re.sub(r'\\r\\n|\\n', " ", word).split()

exclude = string.punctuation
updated_words = ''.join(el for el in " ".join(words) if el not in exclude)\
                  .split()

print(f"Количество различных слов - {len(set(updated_words))}")
