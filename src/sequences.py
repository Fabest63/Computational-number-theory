import math

def sum_multiples(n, i):
    """
    Returns the sum of all multiples of i below n. 
    Complexity: O(n/i) 
    Args: 
        n (int): The upper limit (exclusive). 
        i (int): The number whose multiples are to be summed. 
    """
    return sum(x for x in range(n) if x % i == 0)
