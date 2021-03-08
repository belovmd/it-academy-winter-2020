"""Оформите указанную задачу из прошлых домашних в виде функции
   и покройте тестами. Учтите, что в функцию могут быть переданы
   некорректные значения, здесь может пригодится ‘assertRaises’.
   Не нужно переделывать функцию для того чтобы она ловила все
   возможные ситуации сама.

   Вариант 2: Домашняя 3. Задача 5.
   Уникальные элементы в списке
   Дан список.
   Выведите те его элементы, которые встречаются в списке только один раз
   Элементы нужно выводить в том порядке, в котором они встречаются в списке
"""


import unittest


def task5_from_hw3(lst_=None):
    if lst_ is None:
        lst_ = []
    dct_ = {}
    result = ''

    for element in lst_:
        dct_[element] = dct_.get(element, 0) + 1

    for key, value in dct_.items():
        if value == 1:
            result = f'{result} {key}'

    return result


class HomeworkTask3Test(unittest.TestCase):
    def test_no_arguments(self):
        self.assertEqual(task5_from_hw3(), '')

    def test_regular(self):
        self.assertEqual(
            task5_from_hw3([1, 2, 3, 4, 5]), ' 1 2 3 4 5')

    def test_dict_data(self):
        self.assertEqual(
            task5_from_hw3({'key': 1}), ' key')

    def test_boolean_data(self):
        self.assertEqual(task5_from_hw3([1, 'b', 1, 'b', 4]), ' 4')

    def test_boolean_data_2(self):
        self.assertRaises(TypeError, task5_from_hw3, True)

    def test_number_data(self):
        self.assertRaises(TypeError, task5_from_hw3, 1)


if __name__ == '__main__':
    unittest.main()
