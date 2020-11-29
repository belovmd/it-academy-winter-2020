""" Task 1:
Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
"""


def price_count(rub, kop, count):
    """Подсчет общей суммы покупки

    :param rub: рубли
    :param kop: копейки
    :param count: количество товара
    :return: строка. Общая цена в рублях и копейках
    """
    rubles = rub * count
    kopeck = kop * count

    return f"{rubles + kopeck // 100} рубля(-ей) {kopeck % 100} копеек"


if __name__ == "__main__":
    m = 0
    n = 99
    s = 3

    print(price_count(m, n, s))
