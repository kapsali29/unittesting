import unittest
from src.rps import rps


class TestRPS(unittest.TestCase):
    valid_inputs = list(range(0, 3))
    valid_outputs = ['rock', 'paper', 'scissors']

    def test_valid_input(self):
        inputs = [0, 1, 2]
        for inp in inputs:
            with self.subTest(inp=inp):
                self.assertIn(inp, self.valid_inputs)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            rps(50)

    def test_output(self):
        for idx, item in enumerate(self.valid_outputs):
            with self.subTest(idx=idx, item=item):
                self.assertEqual(rps(idx), item)


if __name__ == "__main__":
    unittest.main()
