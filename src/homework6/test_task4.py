import unittest
import task4


class Test(unittest.TestCase):

    def test_no_arguments(self):
        self.assertEqual(task4.project_euler455(), '')

    def test_arguments(self):
        self.assertIn('n', range(2, 'max_range'))

    def test_boolean_data(self):
        self.assertRaises(TypeError, task4.project_euler455, True)


if __name__ == '__main__':
    unittest.main()