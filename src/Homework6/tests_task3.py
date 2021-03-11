import unittest
from task3 import max_div


class TestMaxDivFunction(unittest.TestCase):

    def test_number_max_div(self):
        list_values = [(10, 2), (16, 16), (12, 4)]
        for value, result in list_values:
            self.assertEqual(max_div(value), result)

    def test_text_max_div(self):
        with self.assertRaises(TypeError):
            max_div('text')
