from src import primes, sequences

def test_prime_checks():
    """Verifies the primality test logic."""
    # Known primes
    assert primes.is_prime(2) is True
    assert primes.is_prime(3) is True
    assert primes.is_prime(5) is True
    assert primes.is_prime(7) is True

    # Known non-primes
    assert primes.is_prime(1) is False
    assert primes.is_prime(4) is False
    assert primes.is_prime(9) is False

def test_max_prime_divisor():
    """Verifies the calculation of the largest prime factor."""
    assert primes.max_prime_divisor(28) == 7        # 28 = 2^2 * 7
    assert primes.max_prime_divisor(18) == 3        # 18 = 2 * 3^2
    assert primes.max_prime_divisor(29) == 29       # Prime number returns itself
    assert primes.max_prime_divisor(13195) == 29
    assert primes.max_prime_divisor(1) is None      # Edge case: 1 has no prime factors
    assert primes.max_prime_divisor(-3) is None     # Edge case: Negatives

def test_sequence_sums(): 
    """Verifies the sum of multiples logic."""
    assert sequences.sum_multiples(10, 3) == 18     # 3 + 6 + 9 = 18
    assert sequences.sum_multiples(20, 5) == 30     # 5 + 10 + 15 = 30
    assert sequences.sum_multiples(15, 15) == 0     # Limit is exclusive

def test_fibonacci_logic():
    """Verifies Fibonacci sequence generation and limits."""
    # Basic sequence checks
    assert sequences.fibonacci(0) == 1
    assert sequences.fibonacci(3) == 2
    assert sequences.fibonacci(5) == 5
    
    # Check limit logic
    assert sequences.fibonacci_number_limit(5, 7) is None   # 5 < 7
    assert sequences.fibonacci_number_limit(5, 3) == 5      # 5 > 3

def test_fibonacci_sum():
    """Verifies the sum of even/odd Fibonacci numbers."""
    assert sequences.fibonacci_sum(5, 1) == 2       # Only 2 is even below 5
    assert sequences.fibonacci_sum(5, 0) == 10      # Sum of all below 5
    assert sequences.fibonacci_sum(10, 0) == 99     # Sum of all below 10