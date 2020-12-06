"""
1.
https://www.hackerrank.com/challenges/write-a-function/problem
Task
Given a year, determine whether it is a leap year
(please refer to the task i=on the site for mote details).
If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
It is only necessary to complete the is_leap function.
"""


def is_leap(year):
    leap = False

    if not year % 400:
        leap = True
    elif not year % 100:
        leap = False
    elif not year % 4:
        leap = True
    else:
        leap = False

    return leap


s = int(input('Please input a year: '))
print(is_leap(s))

"""
2.
https://www.hackerrank.com/challenges/py-if-else/problem
Task
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer, n.

Constraints
1 <= n <= 100

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
"""


# !/bin/python3
if __name__ == '__main__':
    n = int(input('Please input an integer: ').strip())

if n % 2:
    print('Weird')
elif n >= 2 and n <= 5:
    print('Not Weird')
elif n >= 6 and n <= 20:
    print('Weird')
else:
    print('Not Weird')

"""
3.
https://www.hackerrank.com/challenges/the-minion-game/problem
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""


def minion_game(string):
    vowels = 'AEIOU'

    kevin = 0
    stuart = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin += (len(s) - i)
        else:
            stuart += (len(s) - i)

    if kevin > stuart:
        print("Kevin" + str(kevin))
    elif kevin < stuart:
        print("Stuart", str(stuart))
    else:
        print("Draw")

if __name__ == '__main__':


    s = input('Please input a word in upper-case letters: ')
    minion_game(s)
