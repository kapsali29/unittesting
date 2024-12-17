import unittest


class TestCollection(unittest.TestCase):
    def test_sequence(self):
        a = ('h', 'e', 'l', 'l', 'o')
        b = 'hello'
        self.assertSequenceEqual(a, b)

    def test_strings(self):
        self.assertMultiLineEqual('hello', 'hello')

    def test_list(self):
        self.assertListEqual(['a', 'b'], ['a', 'b'])
        self.assertListEqual(['a', '1'], ['a', '1'])

    def test_sets(self):
        self.assertSetEqual({1, 2, 3}, {1, 2, 3})

    def test_tuples(self):
        self.assertTupleEqual((1, 2), (1, 2))

    def test_dicts(self):
        self.assertDictEqual({'key': 1}, {'key': 1})


if __name__ == '__main__':
    unittest.main()
