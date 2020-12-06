""" Task 7.3:
Task name: Where my anagrams at?
Source: CodeWars
Level: 5 kyu
Url: https://www.codewars.com/kata/523a86aa4230ebb5420001e1/python
"""


def find_anagrams(word, words):
    return [_word for _word in words if sorted(word) == sorted(_word)]


if __name__ == '__main__':
    print(find_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))