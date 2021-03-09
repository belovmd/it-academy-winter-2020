import ddt
import task4
import unittest


@ddt.ddt
class TestSuite(unittest.TestCase):

    @ddt.data(
        ('aaa', False),
        (5 + 2j, False),
        (' ', False),
    )
    @ddt.unpack
    def test_type_error(self, num, result):
        with self.assertRaises(TypeError):
            task4.func(num)

    def test_result(self):
        self.assertEqual(task4.func(100), 51)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            task4.func(-2)

    def test_boolean(self):
        with self.assertRaises(ValueError):
            task4.func(False)
