""" Task 6:
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""


def get_reverse(number):
    """
    Вычисление "обратного" целого числа

    :param number: входное число
    :return: число. Цифры в числе идут в обратном порядке
    """
    rev = 0
    while number > 0:
        rev = (10 * rev) + number % 10
        number //= 10
    return rev


if __name__ == "__main__":
    number = 11211
    if get_reverse(number) == number:
        print(f'{number} is palindrome')
    else:
        print(f'{number} not palindrome')
