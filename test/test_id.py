import unittest


class TestIdentity(unittest.TestCase):
    def test_id_same(self):
        a = ["panos", "is"]
        b = a
        self.assertIs(a, b)

    def test_not(self):
        a = ["panos", "is"]
        b = ["panos", "is"]
        self.assertIsNot(a, b)


if __name__ == '__main__':
    unittest.main()
