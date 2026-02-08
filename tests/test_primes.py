import unittest
from src.primes import is_prime

class TestPrimeFunctions(unittest.TestCase):
    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_non_primes(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))

if __name__ == '__main__':
    unittest.main()