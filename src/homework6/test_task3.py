from unittest import TestCase

from ddt import ddt, data, unpack

from . import task3


@ddt
class MyTest(TestCase):

    @data(
        ([2, 3, 4], {2: 1, 3: 1, 4: 1}),
        ([7, 7, 7, 1, 1, 4], {7: 3, 1: 2, 4: 1})
    )
    @unpack
    def test_count_element(self, list_, result_dict):
        """Test: count elements function"""
        result = task3.count_elements(list_)
        self.assertDictEqual(result, result_dict)

    def test_count_element_with_empty_data(self):
        """Test: count element function with empty data"""
        result = task3.count_elements(None)
        self.assertDictEqual(result, {})

    @data(
        ['2:+++', '3++++', '4++++', ],
        ('2:+++', '3++++', '4++++',),
    )
    def test_write_to_file_iterable_object(self, data_):
        """Test: check data arg type"""
        self.assertEqual(True, isinstance(data_, list) or isinstance(data_, tuple))

    def test_write_to_file_with_non_string_items(self):
        """Test: write to file with non string items"""
        self.assertRaises(TypeError, task3.write_to_file, [1, 2, 3], 'test.txt')

    def test_write_to_file_with_empty_data(self):
        self.assertRaises(TypeError, task3.write_to_file, None, 'test.txt')
