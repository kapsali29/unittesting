import unittest


class TestElement(unittest.TestCase):

    def test_isin(self):
        a = 1
        al = [1, 2, 34, 5, 6]
        self.assertIn(a, al)
        self.assertNotIn(55, al)


if __name__ == "__main__":
    unittest.main()

# also you can run the tests as follows
# python -m unittest test.test_element
# python -m unittest test.test_element.TestElement
# python -m unittest test.test_element.TestElement.test_isin
