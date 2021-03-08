from unittest import TestCase

from ddt import data
from ddt import ddt
from ddt import unpack

from . import task4


@ddt
class MyTest(TestCase):

    @data(
        (11, (6, 2, 3.0),),
        (100, (30, 8, 3.75)),
        (500, (210, 48, 4.375)),
        (1000, (210, 48, 4.375)),
    )
    @unpack
    def test_euler_function_with_different_number(self, number, result_data):
        """Test: function with different number """
        result = task4.euler_function_maximum(number)
        self.assertTupleEqual(result, result_data)

    def test_euler_function_for_number_less_than_2(self):
        """Test: function for number less than two"""
        result = task4.euler_function_maximum(1)
        self.assertTupleEqual(result, tuple())

    @data(
        1001,
        10000,
        100000,
    )
    def test_euler_function_for_number_more_than_1000(self, number):
        self.assertRaises(task4.TooLongException,
                          task4.euler_function_maximum,
                          number)

    @data(
        [123, ],
        (1, 2, 3),
        dict(),
    )
    def test_euler_function_with_non_integer_parameter(self, number):
        self.assertRaises(TypeError,
                          task4.euler_function_maximum,
                          number)
