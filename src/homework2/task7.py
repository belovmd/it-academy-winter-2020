import re
import string


"""
    Task 7. Зарегистрируйтесь на одном (или нескольких) из сайтов:

    https://py.checkio.org/, https://www.codewars.com, https://www.hackerrank.com/, https://acmp.ru

    Решите 1-5 задач уровня Elementary и Advanced.
    Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.


    Задачи взяты с сайта https://www.codewars.com
"""


"""
    Task 7-1
    Money, Money, Money. (7 kyu)

    Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does, he wants to know 
    how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a 
    desired sum of money 'D'.
    The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly. After paying taxes 
    'T' for the year the new sum is re-invested.

    Note to Tax: not the invested principal is taxed, but only the year's accrued interest

    Example:
    Let P be the Principal = 1000.00
    Let I be the Interest Rate = 0.05
    Let T be the Tax Rate = 0.18
    Let D be the Desired Sum = 1100.00

    After 1st Year -->
      P = 1041.00
    After 2nd Year -->
      P = 1083.86
    After 3rd Year -->
      P = 1128.30

    Thus Mr. Scrooge has to wait for 3 years for the initial principal to amount to the desired sum.

    Your task is to complete the method provided and return the number of years 'Y' as a whole in
    order for Mr. Scrooge to get the desired sum.

    Assumption: Assume that Desired Principal 'D' is always greater than the initial principal.
    However it is best to take into consideration that if Desired Principal 'D' is equal to Principal
    'P' this should return 0 Years.
"""


def calculate_years(principal, interest, tax, desired):
    p_sum = principal
    years = 0

    while p_sum < desired:
        profit = p_sum * interest
        p_sum = p_sum + (profit - (profit * tax))
        years += 1

    return years


"""
    Task 7-2.
    IQ Test. (6 kyu)

    Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers
    differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check
    his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a
    position of this number.

    ! Keep in mind that your task is to help Bob solve a real IQ test,
    which means indexes of the elements start from 1 (not 0)

    Examples:
    iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
    iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""


def iq_test(numbers):
    list_of_numbers = numbers.split(" ")
    odds = []
    evens = []

    for num in list_of_numbers:
        index = list_of_numbers.index(num)

        if int(num) % 2:
            odds.append(index + 1)
        else:
            evens.append(index + 1)

    if len(odds) == 1:
        return odds[0]
    else:
        return evens[0]


"""
    Task 7-3
    Highest Scoring Word (6 kyu)

    Given a string of words, you need to find the highest scoring word.
    Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
    You need to return the highest scoring word as a string.
    If two words score the same, return the word that appears earliest in the original string.
    All letters will be lowercase and all inputs will be valid.

    Examples:
    high('man i need a taxi up to ubud') // 'taxi'
    high('what time are we climbing up the volcano') // 'volcano'
    high('take me to semynak') // 'semynak'
"""


def high(x):
    alp = string.ascii_lowercase

    list_of_words = x.split(" ")
    score_list = {}

    for word in list_of_words:
        score = 0
        for symbol in word:
            score += alp.find(symbol)

        score_list[word] = score

    return max(score_list, key=score_list.get)


"""
    Task 7-4
    +1 Array (6 kyu)

    Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

    the array can't be empty
    only non-negative, single digit integers are allowed
    Return nil (or your language's equivalent) for invalid inputs.

    Examples
    For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
    [4, 3, 2, 5] would return [4, 3, 2, 6]
"""


def up_array(arr):
    if not len(arr):
        return None

    for i in arr:
        if i < 0 or i > 9:
            return None

    num = int(''.join(map(str, arr)))
    num = num + 1

    updated_arr = []

    for i in str(num):
        updated_arr.append(int(i))

    return updated_arr


"""
    Task 7-5
    String incrementer (5 kyu)

    Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

    Examples:
    foo -> foo1
    foobar23 -> foobar24
    foo0042 -> foo0043
    foo9 -> foo10
    foo099 -> foo100

    Attention: If the number has leading zeros the amount of digits should be considered.
"""

regexp = "\d+$"


def increment_string(strng):
    search_in_str = re.search(regexp, strng)
    number_init = search_in_str.group(0) if search_in_str else ""

    num = number_init
    length = len(num)
    accum_number = 1

    if len(num):
        accum_number = int(num) + 1

    number_length = length - len(str(accum_number))

    if number_length:
        num = f"{'0' * number_length}{accum_number}"
    else:
        num = accum_number

    if len(number_init):
        return re.sub(regexp, str(num), strng)
    else:
        return strng + num
