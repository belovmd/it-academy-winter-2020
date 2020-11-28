""" Task 2:
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""
from string import punctuation


def find_longest_work(sentence):
    """Поиск самого длинного слова в предложении.

    :param sentence: входная строка
    :return: строка. Самое длинное слово в предложении
        (в случае если их несколько, самое левое в строке).
    """

    for punct_mark in punctuation:
        sentence = sentence.replace(punct_mark, "")
    words = sentence.split(' ')

    return max(words, key=len)


if __name__ == "__main__":
    input_sentence = (
        "Предложение – это господствующие в русском языке "
        "словосочетания, в которых заключены грамматическое подлежащее и "
        "грамматическое сказуемое."
    )

    print(find_longest_work(input_sentence))
