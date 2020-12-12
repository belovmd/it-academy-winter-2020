import re


"""1. Вам дано положительное целое число. Определите сколько цифр оно имеет.
    Входные данные: Положительное целое число.
    Выходные данные: Целое число.
"""


num = 1000
number_length = 0

while num:
    num //= 10
    number_length += 1

print(number_length)


"""2. Попробуйте выяснить какое количество нулей содержит
    данное число в конце.
    Входные данные: Положительное целое число (int).
    Выходные данные: Целое число (int).
"""


num = 10000
end_zeros = 0

while num % 10 == 0:
    num //= 10
    end_zeros += 1

print(end_zeros)


"""3. Вам дана строка состоящая только из цифр.
    Вам нужно посчитать сколько нулей ("0") находится в начале строки.
    Входные данные: Строка, состоящая только из цифр.
    Выходные данные: Целое число.
    Строка может иметь цифры: 0-9.
"""


str_ = '001090650'
count_zeros = 0

for number in str_:
    if number == str('0'):
        count_zeros += 1
    else:
        break

print(count_zeros)


"""4. Given a year, determine whether it is a leap year.
    If it is a leap year, return the Boolean True, otherwise return False.
"""


year = int(input())


def is_leap():
    if year % 4 == 0 and year % 100:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


print(is_leap())


"""5. Word Order
    Difficulty Medium
    
    You are given  words. Some words may repeat.
    For each word, output its number of occurrences.
    The output order should correspond with the input order
    of appearance of the word.
    See the sample input/output for clarification.

    Constraints:

    The sum of the lengths of all the words do not exceed 10**6.
    All the words are composed of lowercase English letters only.

    Input Format:
        The first line contains the integer, n.
        The next n lines each contain a word.
    
    Output Format:
        Output 2 lines.
        On the first line, output the number of distinct words from the input.
        On the second line, output the number of occurrences for each
        distinct word according to their appearance in the input.
"""


number = int(input())
dct = {}
while number:
    word = input()
    number -= 1
    if word not in dct:
        dct[word] = dct.get(word, 1)
    else:
        dct[word] = dct.get(word, 1) + 1
print(len(dct))
print(*dct.values())


"""6. You and Fredrick are good friends.
    Yesterday, Fredrick received  credit cards from ABCD Bank.
    He wants to verify whether his credit card numbers are valid or not.
    You happen to be great at regex so he is asking for your help!

    A valid credit card from ABCD Bank has the following characteristics:

    ► It must start with a 4, 5 or 6.
    ► It must contain exactly 16 digits.
    ► It must only consist of digits (0-9).
    ► It may have digits in groups of 4, separated by one hyphen "-".
    ► It must NOT use any other separator like ' ' , '_', etc.
    ► It must NOT have 4 or more consecutive repeated digits.
    
    Input Format
        The first line of input contains an integer N.
        The next N lines contain credit card numbers.
    
    Output Format
        Print 'Valid' if the credit card number is valid.
        Otherwise, print 'Invalid'. Do not print the quotes.
"""


def is_card_valid(cards):
    match = r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$'
    if re.match(match, cards):
        return True
    else:
        return False


N = int(input())

for _ in range(N):
    cards = input()
    print('Valid' if is_card_valid(cards) else "Invalid")
