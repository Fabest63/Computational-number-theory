def is_pal(n):
    """
    Checks if a given number is a palindrome.
    
    Complexity: O(d), where d is the number of digits in n.
    
    Args:
        n (int): The number to check. 
    Returns:
        bool: True if n is a palindrome, False otherwise.
    """
    s = str(n)
    inv_s = s[::-1]
    return s == inv_s

def max_pal_num(n):
    """
    Finds the largest palindrome number that is product of two numbers of n digits.
    Complexity: O(10^(2n)), where n is the number of digits.
    Args:
        n (int): The number of digits for the factors.
    Returns:        int: The largest palindrome product of two n-digit numbers.
    """
    if n < 1:
        return None
    else:
        max_palindrome = 0
        for i in range(10**(n-1), 10**n):
            for j in range(i, 10**n):
                product = i * j
                if is_pal(product) and product > max_palindrome:
                    max_palindrome = product
        return max_palindrome
