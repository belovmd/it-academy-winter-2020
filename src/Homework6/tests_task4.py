import unittest
from task4 import numerator

from fractions import Fraction


class TestNumeratorFunc(unittest.TestCase):

    def test_numerator(self):
        self.assertEqual(numerator(8), Fraction(2, 5))

    def test_text_numerator(self):
        with self.assertRaises(TypeError):
            numerator("text")
