import math

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime using an optimized trial division.
    
    Complexity: O(sqrt(n))
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
      
    return True

def max_prime_dividor(n:int):
    """
    Finds the largest prime divisor of a given number.
    
    Complexity: O(sqrt(n))
    
    Args:
        n (int): The number to find the largest prime divisor for.
        
    Returns:
        int: The largest prime divisor of n, or None if n is less than 2.
    """
    if n < 2:
        return None
    
    max_prime = -1
    
    # Check for number of 2s that divide n
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    
    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
            
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        max_prime = n
        
    return max_prime