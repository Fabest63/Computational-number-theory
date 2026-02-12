import unittest
from src.primes import is_prime
from src.sequences import sum_multiples
from src.sequences import fibonacci
from src.sequences import fibonacci_number_limit
from src.sequences import fibonacci_sum


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
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 1)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
    
    def test_fibonacci_number_limit(self):
        self.assertEqual(fibonacci_number_limit(5, 7), None) # 5 < 7
        self.assertEqual(fibonacci_number_limit(5, 3), 5) # 5 > 3
        self.assertEqual(fibonacci_number_limit(4, 4), None) # 3 < 4
        self.assertEqual(fibonacci_number_limit(4, 3), None) # 3 <= 3

    def test_fibonacci_sum(self):
        self.assertEqual(fibonacci_sum(5, 1), 2) # 2 = 2
        self.assertEqual(fibonacci_sum(5, 0), 10) # 1 + 1 + 3 + 5 = 10
        self.assertEqual(fibonacci_sum(10, 1), 44) # 2 + 8 + 34 = 44
        self.assertEqual(fibonacci_sum(10, 0), 99) # 1 + 1 + 3 + 5 + 13 + 21 = 99

if __name__ == '__main__':
    unittest.main()