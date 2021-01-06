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
updated_words = ''.join(symbol for symbol in " ".join(words) if symbol not in exclude)\
                  .split()

print(f"Количество различных слов - {len(set(updated_words))}")
