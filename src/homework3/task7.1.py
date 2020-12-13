""" Task 7.1: Шоколадка (часть 1)
Определите, можно ли одним разломом отделить
от шоколадки кусок площадью ровно k.
"""


def is_break(width, height, piece_area):
    """

    :param width:
    :param height:
    :param piece_area:
    :return:
    """

    chocolate_area = width * height

    if piece_area > chocolate_area:
        print('Площадь шоколадки меньше, чем площадь кусочка, который вы'
              ' хотите отломать =( .'
              )

        return False

    if piece_area == chocolate_area:
        print('Вам ничего не нужно ломать, '
              'просто возьмите её и съешьте =) .'
              )

        return False

    if (not piece_area % width) or (not piece_area % height):
        print(f'Вы можете отломать от шоколадки '
              f'кусочек площадью {piece_area} =)'
              )

        return True

    print(f'К сожалению кусочек площадью {piece_area} Вам не отломать =(')
    return False


if __name__ == "__main__":
    m, n = 3, 5
    k = 7

    print(is_break(m, n, k))
