""" Task 3: Максимум функции Эйлера, Задача 69
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для
определения количества чисел, меньших n, которые взаимно просты с n.
К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с
девятью, φ(9)=6.

Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.

Примечание: задача обобщена для n ≤ 1000 (это решение задачи "в лоб")
"""


class TooLongException(Exception):
    ...


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def euler_function_maximum(number):
    """Поиск максимального значение функции Эйлера

    :param number: целое число
    :return: кортеж. Формат:
    (
        число n,
        значение функции Эйлера,
        значение функции n/φ(n)
    )
    При n <= 1 функция возвращает пустой кортеж
    """

    if number < 2:
        return tuple()
    elif number > 1000:
        raise TooLongException('Для данного параметра вычисления будут '
                               'проводится слишком долго.')
    elif not isinstance(number, int):
        raise TypeError

    function_results = list()
    for n in range(2, number):
        prime_count = 1
        for i in range(2, n):
            if gcd(i, n) == 1:
                prime_count += 1
        function_results.append(
            (n, prime_count, n / prime_count)
        )

    return max(function_results, key=lambda item: item[2])


if __name__ == "__main__":
    result = euler_function_maximum(1001)
    print(f'n={result[0]}    φ(n)={result[1]}     n/φ(n)={result[2]}')
