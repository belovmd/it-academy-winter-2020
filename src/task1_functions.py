"""
4. Пары элементов
Дан список чисел.
Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу,
образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def pairs(numbers):
    # numbers = '1 1 2 2 67 67 1 1 2'
    list1 = numbers.split()
    pairs = 0
    numbers_amount = {element: list1.count(element) for element in list1}
    for key in numbers_amount:
        n = 0
        while n < numbers_amount[key] - 1:
            n += 1
            pairs += n
    return print(pairs)


"""
5. Уникальные элементы в списке
Дан список.
Выведите те его элементы, которые встречаются
в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""


def unique(initial_list):
    # initial_list = [2, 2, 'abc', 79, 'k', 1, 67, 'k']
    result_list = []
    numbers_amount = {element: initial_list.count(element) for element in initial_list}
    for key in numbers_amount:
        if numbers_amount[key] == 1:
            result_list.append(key)
    return print(result_list)


"""
6. Упорядоченный список.
Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть
списка, не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""


def order(initial_list):
    # initial_list = [1, 45, 67, 43, 43, 43, 0, 7, 0, 4]
    for element in initial_list:
        if not element:
            initial_list.remove(element)
            initial_list.append(0)
    return print(initial_list)
