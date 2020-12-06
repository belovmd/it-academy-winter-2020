""" Task 7.1:
Task name: Merge the Tools!
Source: HackerRank
Level: Medium
Url: https://www.hackerrank.com/challenges/merge-the-tools/problem
"""


def get_unique_substring(segment):
    unique_symbols = []
    for symbol in segment:
        if symbol not in unique_symbols:
            unique_symbols.append(symbol)

    return ''.join(unique_symbols)


def merge_the_tools(string, k):
    """
    Вычисление уникальных подстрок для сегментов строки

    :param string: входная строка
    :param k: количество сегментов (разбиений)
    :return: список, содержащий уникальные подстроки для сегментов строки
    """
    # разбиваем строки на части
    segments = [string[start: start + k] for start in range(0, len(string), k)]
    #
    subsequences = list(map(lambda x: get_unique_substring(x), segments))

    return subsequences


if __name__ == "__main__":

    string = "AABCAAADADAA"
    k = 4

    if not len(string) % k:
        print(merge_the_tools(string, k))
    else:
        print('Exit')
