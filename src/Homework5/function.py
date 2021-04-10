'''
    Напишите программу, которая считает общую цену.
    Вводится M рублей и N копеек цена, а также количество S
    товара Посчитайте общую цену в рублях и копейках за L товаров.
'''


def task_1(rubles=1, penny=2, product=3):
    penny_product = (penny * product) % 100
    rubles_product = (product * rubles) + (product * penny) // 100
    print(rubles_product, 'p.', penny_product, 'k.')
    return (rubles_product, 'p.', penny_product, 'k.')


"""
    Вводится строка. Требуется удалить из нее повторяющиеся
    символы и всепробелы. Например, если было введено "abc
    cde def", то должно быть выведено "abcdef".
"""


def task_2():
    str_ = 'abc cde def'
    new_str = ''

    for letter in str_:
        if letter not in new_str and letter != ' ':
            new_str += letter
    print(new_str)
    return new_str


"""
    Даны два списка чисел.Посчитайте,сколько
    различных чисел содержится одновременно
    как в первом списке, так и во втором
"""


def task_3():
    list_1 = [1, 2, 3, 4]
    list_2 = [3, 4, 5]
    set_1 = set(list_1) & set(list_2)
    print(set_1)
    return len(set_1)
