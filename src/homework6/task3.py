""" Оформите указанную задачу из прошлых домашних в виде функции и покройте
    тестами. Учтите, что в функцию могут быть переданы некорректные значения,
    здесь может пригодится ‘assertRaises’. Не нужно переделывать функцию для
    того чтобы она ловила все возможные ситуации сама.

    Борисенко Денис Вариант 3.	Домашняя 3. Задача 4.

    'Дан список чисел. Посчитайте, сколько в нем пар элементов,
    равных друг другу. Считается, что любые два элемента, равные друг другу
    образуют одну пару, которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.'
"""


import unittest
import home_work34


class HomeworkTest(unittest.TestCase):
    def test_no_arguments(self):
        self.assertEqual(home_work34.home_work(), '')

    def test_split(self):
        string_num = '1 1 2 2 3 3 3 4 4 4 4'
        self.assertEqual(string_num.split(), [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

    def test_boolean_data(self):
        self.assertRaises(TypeError, home_work34.home_work, True)

    def test_number(self):
        self.assertRaises(TypeError, home_work34.home_work, 11)


if __name__ == '__main__':
    unittest.main()