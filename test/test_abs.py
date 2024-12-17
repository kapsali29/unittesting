import unittest


class TestAbs(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(abs(10), 10)

    def test_negative(self):
        self.assertEqual(abs(-10), 10)

    def test_zero(self):
        self.assertEqual(abs(0), 0)


if __name__ == "__main__":
    unittest.main()
