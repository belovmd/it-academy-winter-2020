# Оформите указанную задачу из прошлых домашних
# в виде функции и покройте тестами. Учтите,
# что в функцию могут быть переданы некорректные
# значения, здесь может пригодится ‘assertRaises’.
# Не нужно переделывать функцию для того чтобы она
# ловила все возможные ситуации сама.
import ddt
import random
import task2
import unittest
from unittest.mock import patch


@ddt.ddt
class TestSuite(unittest.TestCase):

    @ddt.data(
        (0, False),
        (-5, False),
        (11, False),
        ('aaa', False),
    )
    @ddt.unpack
    def test_type_error(self, num, result):
        """Test {} input error {}"""
        with self.assertRaises(TypeError):
            task2.guess(num)

    @patch('task2.random_', return_value=random.randrange(1, 2))
    def test_range_random(self, random_):
        self.assertEqual(random_(), 1)

    def test_boolean_data(self):
        self.assertRaises(TypeError, task2.guess, False)
