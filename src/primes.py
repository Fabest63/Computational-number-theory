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