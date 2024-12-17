import unittest


class TestEven(unittest.TestCase):

    def test_if_is_even(self):
        for number in [2, 4, 6, -2, 10, 12]:
            with self.subTest(number=number):
                self.assertEqual(number % 2, 0)

    def test_if_is_odd(self):
        for number in [1, 3, 5, 7, 11, -11, -13, 15]:
            with self.subTest(number=number):
                self.assertEqual(number % 2, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
