import unittest
from src.age import categorize_by_age


class TestCategorizer(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorize_by_age(5), 'Child')

    def test_adolescent(self):
        self.assertEqual(categorize_by_age(15), 'Adolescent')

    def test_adult(self):
        self.assertEqual(categorize_by_age(30), 'Adult')

    def test_golden_age(self):
        self.assertEqual(categorize_by_age(70), 'Golden age')

    def test_negative_age(self):
        self.assertEqual(categorize_by_age(-1), 'Invalid age: -1')

    def test_too_old(self):
        self.assertEqual(categorize_by_age(151), 'Invalid age: 151')

    def test_boundaries(self):
        self.assertEqual(categorize_by_age(9), 'Child')
        self.assertEqual(categorize_by_age(10), 'Adolescent')
        self.assertEqual(categorize_by_age(18), 'Adolescent')
        self.assertEqual(categorize_by_age(19), 'Adult')
        self.assertEqual(categorize_by_age(65), 'Adult')
        self.assertEqual(categorize_by_age(66), 'Golden age')
        self.assertEqual(categorize_by_age(150), 'Golden age')
        self.assertEqual(categorize_by_age(151), 'Invalid age: 151')


if __name__ == "__main__":
    unittest.main()
