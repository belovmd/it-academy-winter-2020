""" Task 7.3:
Task name: Where my anagrams at?
Source: CodeWars
Level: 5 kyu
Url: https://www.codewars.com/kata/523a86aa4230ebb5420001e1/python

What is an anagram? Well, two words are anagrams of each other if
they both contain the same letters. For example:

'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from
a list. You will be given two inputs a word and an array with
words. You should return an array of all the anagrams or an
empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
=> ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
=> ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer'])
=> []
"""


def find_anagrams(word, words):
    """Поиск анаграмм слова word среди слов в списке words

    :param word: входное слово
    :param words: список слов
    :return: список. В списке находятся аннаграммы
        слова word
    """
    return [_word for _word in words if sorted(word) == sorted(_word)]


if __name__ == '__main__':
    print(find_anagrams('racer',
                        ['crazer', 'carer', 'racar', 'caers', 'racer']
                        )
          )
