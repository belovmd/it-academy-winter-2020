from unittest import mock
from unittest import TestCase
import task3
import unittest


class Tests(TestCase):
    """For Positive tests"""
    students_input = [
        3,
        2, 'Russian', 'English',
        3, 'Russian', 'Belarusian', 'English',
        3, 'Russian', 'Italian', 'French',
    ]
    one_student_input = [
        1,
        1, 'Russian',
    ]
    one_language_input = [
        3,
        1, 'English',
        1, 'English',
        1, 'English',
    ]

    """For Negative tests"""
    nobody_knows_languages_input = [
        4,
        2, 'English', 'Russian',
        1, 'Polish',
        3, 'Japanese', 'Turkish', 'Ukrainian',
        1, 'Urdu'
    ]
    student_dont_know_languages_input = [
        3,
        1, 'English',
        3, 'Polish', 'Ukrainian', 'English',
        0,
    ]
    wrong_students_amount_input = [
        'English',
        2, 'English', 'Russian'
    ]

    """Positive tests"""

    @mock.patch('builtins.input', side_effect=students_input)
    def test_students_languages_info(self, mock_input):
        """Several students know several languages,
        languages should displayed in alphabet order"""
        result = task3.students_languages_info()
        expected_result = '1\nRussian\n5\nBelarusian, English, French, Italian, Russian'
        self.assertEqual(result, expected_result)

    @mock.patch('builtins.input', side_effect=one_student_input)
    def test_one_student(self, mock_input):
        """One student knows one language"""
        result = task3.students_languages_info()
        expected_result = '1\nRussian\n1\nRussian'
        self.assertEqual(result, expected_result)

    @mock.patch('builtins.input', side_effect=one_language_input)
    def test_one_language(self, mock_input):
        """Several students know one language"""
        result = task3.students_languages_info()
        expected_result = '1\nEnglish\n1\nEnglish'
        self.assertEqual(result, expected_result)

    """Negative tests"""

    @mock.patch('builtins.input', side_effect=nobody_knows_languages_input)
    def test_nobody_knows_languages(self, mock_input):
        """Nobody knows the same language,
        languages should displayed in alphabet order"""
        result = task3.students_languages_info()
        expected_result = '0\n7\nEnglish, Japanese, Polish, Russian, Turkish, Ukrainian, Urdu'
        self.assertEqual(result, expected_result)

    @mock.patch('builtins.input', side_effect=student_dont_know_languages_input)
    def test_student_dont_know_languages(self, mock_input):
        """Student doesn't know any language,
        languages should displayed in alphabet order"""
        result = task3.students_languages_info()
        expected_result = '0\n3\nEnglish, Polish, Ukrainian'
        self.assertEqual(result, expected_result)

    @mock.patch('builtins.input', side_effect=wrong_students_amount_input)
    def test_wrong_students_amount(self, mock_input):
        """The number of students is not a number"""
        with self.assertRaises(ValueError):
            try:
                task3.students_languages_info()
            except ValueError as e:
                self.assertEqual(e.args, ("The number of students should be a number", ))
                raise


if __name__ == '__main__':
    unittest.main()
