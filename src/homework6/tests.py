from task4 import Problem
import task3
import unittest


class HomeworkTest(unittest.TestCase):
    def test_no_arguments(self):
        self.assertEqual(task3.task5_from_hw3(), '')

    def test_regular(self):
        self.assertEqual(task3.task5_from_hw3([1, 2, 3, 4, 5]), ' 1 2 3 4 5')

    def test_dict_data(self):
        self.assertEqual(task3.task5_from_hw3({'key': 1}), ' key')

    def test_boolean_data(self):
        self.assertEqual(task3.task5_from_hw3([1, 'b', 1, 'b', 4]), ' 4')

    def test_boolean_data(self):
        self.assertRaises(TypeError, task3.task5_from_hw3, True)

    def test_number_data(self):
        self.assertRaises(TypeError, task3.task5_from_hw3, 1)


class HomeworkTest(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(Problem(1).solve(), 571)


def test_regular_2(self):
    self.assertEqual(Problem(2).solve(), 613658361)


def test_regular_3(self):
    self.assertEqual(Problem(3).solve(), 1229737624)


def test_regular_4(self):
    self.assertEqual(Problem(0).solve(), 1)


def test_float(self):
    self.assertRaises(TypeError, Problem(3.5).solve)


def test_list(self):
    self.assertRaises(TypeError, Problem([1, 2, 3]).solve)


def test_tuple(self):
    self.assertRaises(TypeError, Problem((1, 2, 3)).solve)


def test_boolean(self):
    self.assertEqual(Problem(True).solve(), 571)


def test_boolean(self):
    self.assertEqual(Problem(False).solve(), 1)


if __name__ == '__main__':
    unittest.main()
