import math

def sum_multiples(n: int, i: int) -> int:
    """
    Returns the sum of all multiples of i below n. 
    Complexity: O(n/i) 
    Args: 
        n (int): The upper limit (exclusive). 
        i (int): The number whose multiples are to be summed. 
    """
    return sum(x for x in range(n) if x % i == 0)

def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number. 
    Complexity: O(n) 
    Args: 
        n (int): The index of the Fibonacci number to return. 
    Returns:
        The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("The index n must be a non-negative integer.")
    elif n <= 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1 ):
            a, b = b, a + b
        return b
    
def fibonacci_number_limit(n: int, m: int):
    """
    Returns the nth Fibonacci number only if it is strictly greater than m.
    Otherwise, returns None.

    Complexity: O(n)

    Args:
        n (int): The index of the Fibonacci number to generate.
        m (int): The threshold value. The result must be greater than this.

    Returns:
        int: The nth Fibonacci number if it exceeds m.
        None: If the number is less than or equal to m.
    """
    a = fibonacci(n)
    if a > m:
        return a
    else:
        return None

def fibonacci_sum(n: int, i: int) -> int:
    """
    Returns the sum of even or odd Fibonacci numbers up to index n. 
    Complexity: O(n) 
    Args: 
        n (int): The upper index limit of the Fibonacci sequence (inclusive). 
        i (int): Control flag. If 1, sums even values. Otherwise, sums odd values. 
    """
    total_sum = 0
    a, b = 0, 1  # Initialize F_0 and F_1

    for _ in range(n+1):
        # Check parity of the current Fibonacci number 'a'
        if i == 1:
            # Case: Sum even numbers
            if a % 2 == 0:
                total_sum += a
        else:
            # Case: Sum odd numbers
            if a % 2 != 0:
                total_sum += a
        
        # Calculate the next Fibonacci number
        a, b = b, a + b

    return total_sum
    
