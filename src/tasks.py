import string


"""
    Task 4 from Homework 2.
    
    Посчитать количество строчных (маленьких) и прописных (больших)
    букв в введенной строке.
    Учитывать только английские буквы.
"""


def lowers_and_uppers(str_="1914 translation by H. Rackham"):
    lowers, uppers = 0, 0

    for letter in str_:
        if letter in string.ascii_lowercase:
            lowers += 1
        elif letter in string.ascii_uppercase:
            uppers += 1

    return f"Количество строчных букв: {lowers}, " \
           f"количество пописных букв: {uppers}"


"""
    Task 6 from Homework 2.

    Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).
    Число положительное целое, произвольной длины.
    Задача требует работать только с числами (без конвертации числа в строку
    или что-нибудь еще)
"""


def is_palindrome(number=1001):
    revert_number = 0
    n = number

    while n > 0:
        revert_number = (revert_number * 10) + (n % 10)
        n //= 10

    if revert_number == number:
        return f"Число {number} является палиндромом"
    else:
        return f"Число {number} не является палиндромом"


"""
    Task 4 from Homework 3.
    
    Пары элементов
    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
    другу. Считается, что любые два элемента, равные друг другу образуют одну
    пару, которую необходимо посчитать.
    
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def count_pairs(sting_of_numbers="5 5 8 8 8 1 4"):
    counting_numbers = {}
    pairs = {}

    count = 0
    counted_elms = set()

    for num in sting_of_numbers.split():
        counting_numbers[num] = counting_numbers.get(num, 0) + 1

        if counting_numbers[num] > 1:
            if num in counted_elms:
                count -= pairs[num]

            pairs[num] = pairs.get(num, 0) + (counting_numbers[num] - 1)

            count += pairs[num]
            if num not in counted_elms:
                counted_elms.add(num)

    return f"Количество пар - {count}"
