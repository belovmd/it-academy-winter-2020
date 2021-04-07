import unittest
from task3 import get_countries
from task3 import get_country_cities


class TestTask(unittest.TestCase):

    def test_get_country_cities_empty(self):
        result = get_country_cities()
        self.assertEqual(result, {})

    def test_get_country_cities_iteration(self):
        result = get_country_cities('Беларусь Могилев', 'Россия Москва')

        self.assertIsInstance(result, dict)

        self.assertIn('Беларусь', result)
        self.assertIn('Россия', result)

        self.assertIsInstance(result['Беларусь'], list)
        self.assertIsInstance(result['Россия'], list)

        self.assertEqual(len(result['Беларусь']), 2)
        self.assertEqual(len(result['Россия']), 1)

        self.assertIn('Минск', result['Беларусь'])
        self.assertIn('Могилев', result['Беларусь'])

        self.assertIn('Москва', result['Россия'])

    def test_get_countries_empty(self):
        result = get_countries('Беларусь Минск')
        self.assertNotEqual(result, {})
        self.assertEqual(result, [])


if __name__ == '__main__':

    unittest.main()
