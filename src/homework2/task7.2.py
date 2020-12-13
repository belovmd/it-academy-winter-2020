""" Task 7.2:
Task name: Merge the Tools!
Source: HackerRank
Level: Medium
Url: https://www.hackerrank.com/challenges/merge-the-tools/problem

Consider the following:
- A string, "s" , of length "n" where s = c_0c_1 ... c_n-1 .
- An integer, k , where k is a factor of n.
We can split "s" into "n/k" substrings where each subtring, "t_i",
consists of a contiguous block of "k" characters in "s". Then, use
each "t_i" to create string u_i such that:
- The characters in "u_i" are a subsequence of the characters in "t_i".
- Any repeat occurrence of a character is removed from the string
  such that each character in "u_i" occurs exactly once. In other words,
  if the character at some index "j" in "t_i" occurs at a previous index
  "<j" in "t_i", then do not include the character in string "u_i".
Given "s" and "k", print "n/k" lines where each line "i" denotes string "u_i".

Example
s = 'AAABCADDE'
k = 3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'.
The first substring is all 'A' characters, so u_1='A' . The second substring
has all distinct characters, so u_2='BCA'. The third substring has 2 different
characters, so u_3='DE'. Note that a subsequence maintains the original order
of characters encountered. The order of characters in each subsequence shown
is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:
- string s: the string to analyze
- int k: the size of substrings to analyze
"""


def get_unique_substring(segment):
    unique_symbols = []
    for symbol in segment:
        if symbol not in unique_symbols:
            unique_symbols.append(symbol)

    return ''.join(unique_symbols)


def merge_the_tools(string, k):
    """Вычисление уникальных подстрок для сегментов строки

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
