import unittest

from src.prime_v1 import is_prime
from src.prime_v2 import is_prime as is_prime_v2


class TestIfPrime(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(10))

    def test_exception(self):
        with self.assertRaises(ValueError):
            is_prime_v2(-1)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_prime_v2("A")


if __name__ == '__main__':
    unittest.main()
