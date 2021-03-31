
import unittest
from task3 import func


class TestStringMethods(unittest.TestCase):

    def test_func(self):
        result = func('1 1')
        self.assertNotEqual(result, {})
        self.assertEqual(result, ('1'))
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()

unittest.main()
