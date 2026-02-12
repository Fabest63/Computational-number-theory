import unittest
from src.primes import is_prime
from src.sequences import sum_multiples

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

    def test_sequences_sum(self): 
        self.assertEqual(sum_multiples(10, 3), 18) # 0 + 3 + 6 + 9 
        self.assertEqual(sum_multiples(20, 5), 30) # 0 + 5 + 10 + 15
        self.assertEqual(sum_multiples(15, 15), 0) # 0

if __name__ == '__main__':
    unittest.main()