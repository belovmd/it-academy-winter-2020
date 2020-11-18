# Output
import itertools

print('Hello, world!')

# Input, assignment
name = input('What is your name?\n')
print('Hi, %s.' % name)

# For loop, built-in enumerate function, new style formatting
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = [babies, parents + babies]

# Dictionaries, generator expressions
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)

# Triple-quoted strings, while loop
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print(REFRAIN % (bottles_of_beer, bottles_of_beer,
                     bottles_of_beer - 1))
    bottles_of_beer -= 1


# Classes
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0


my_account = BankAccount(15)
my_account.withdraw(50)
print(my_account.balance, my_account.overdrawn())

# 8-Queens Problem (recursion)
BOARD_SIZE = 8


def under_attack(col, queens):
    left = right = col
    for r, c in reversed(queens):
        left, right = left - 1, right + 1
        if c in (left, col, right):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]
    smaller_solutions = solve(n - 1)
    return [solution + [(n, a + 1)]
            for a in range(BOARD_SIZE)
            for solution in smaller_solutions
            if not under_attack(a + 1, solution)]


for answer in solve(BOARD_SIZE):
    print(answer)

# itertools
# noqa from itertools import groupby
lines = '''
This is the
first paragraph.

This is the second.
'''.splitlines()
# Use itertools.groupby and bool to return groups of
# consecutive lines that either have content or don't.
for has_chars, frags in itertools.groupby(lines, bool):
    if has_chars:
        print(' '.join(frags))


# PRINTS:
# This is the first paragraph.
# This is the second.

# Doctest-based testing
def median(pool):
    """Statistical median to demonstrate doctest.

    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])

    6 #change to 7 in order to pass the test

    """
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2


if __name__ == '__main__':
    import doctest

    doctest.testmod()
