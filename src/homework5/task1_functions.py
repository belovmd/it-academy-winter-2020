"""1. Напишите программу, которая считает общую цену.
    Вводится M рублей и N копеек цена, а также количество S товара.
    Посчитайте общую цену в рублях и копейках за S товаров.
"""


def total_price():
    """Calculate the total price.

    :return: the total price.
    """
    m = 21
    n = 32
    s = 2
    rubles = ((m * 100 + n) * s) // 100
    kopecks = ((m * 100 + n) * s) % 100
    total_sum = str(rubles) + ' rubles ' + str(kopecks) + ' kopecks'

    print(total_sum)


if __name__ == '__main__':
    total_price()


"""2. Упорядоченный список.
    Дан список целых чисел. Требуется переместить все ненулевые элементы
    в левую часть списка, не меняя их порядок, а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя, дополнительный список
    использовать нельзя, задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список.
"""


def trailing_zeros():
    """Move zeros to the end of a list.

    :return: a sorted list.
    """
    lst = [1, 0, 3, 0, 0, 0, 4, 0, 0, 0, 3, 5, 0, 0, 0, 6, 2]
    for element in lst:
        if not element:
            lst.remove(element)
            lst.append(element)
    print(lst)


if __name__ == '__main__':
    trailing_zeros()


"""3. Определите, является ли число палиндромом.
    Число положительное целое, произвольной длины.
    Задача требует работать только с числами (без конвертации
    числа в строку или что-нибудь еще).
"""


def palindrome():
    """Define, if a number is a palindrome.

    :return: a string, 'yes' or 'no'.
    """
    number = 12321
    temp_num = number
    reverse_num = 0

    while temp_num:
        digit = temp_num % 10
        reverse_num = reverse_num * 10 + digit
        temp_num //= 10

    if number == reverse_num:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    palindrome()
