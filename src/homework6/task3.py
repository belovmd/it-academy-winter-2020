"""Оформите указанную задачу из прошлых домашних в виде функции и покройте
    тестами. Учтите, что в функцию могут быть переданы некорректные значения,
    здесь может пригодится ‘assertRaises’. Не нужно переделывать функцию для
    того чтобы она ловила все возможные ситуации сама.
"""
import src.homework6.task3_func as func
import unittest
import ddt

import src.homework6.task3_additional as funcs


@ddt.ddt
class TestFuncRunner(unittest.TestCase):

    @ddt.data('palindrome')
    def test_in_args(self, function_):
        result = dir(funcs)
        self.assertIn(function_, result)

    @ddt.data(
        ('palindrome', funcs.palindrome()),
        ('total_price', funcs.total_price()),
        ('trailing_zeros', funcs.trailing_zeros()),
    )
    @ddt.unpack
    def test_function_in_args(self, args, expected):
        result = func.runner(args)
        self.assertEqual(result, expected)

    def test_attribute_error(self):
        with self.assertRaises(AttributeError):
            func.runner('fibonacci')

    def test_type_error(self):
        with self.assertRaises(TypeError):
            func.runner(123)

    def test_type_error2(self):
        with self.assertRaises(TypeError):
            func.runner('__name__')
