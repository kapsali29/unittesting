import unittest

from src.stack import Stack


## Test Fixtures
## You can create a single instance of the class for all the tests.

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_push(self):
        stack = self.stack
        stack.push(1)
        self.assertEqual(stack.__len__(), 1)

    def test_pop(self):
        stack = self.stack
        stack.push(12)
        poped_item = stack.pop()
        self.assertEqual(poped_item, 12)


if __name__ == "__main__":
    unittest.main()
