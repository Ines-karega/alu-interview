#!/usr/bin/python3
"""
Module for calculating minimum operations to reach n 'H' characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations to result in exactly n H's.

    The only operations allowed are 'Copy All' and 'Paste'.
    Uses prime factorization: the sum of all prime factors of n equals
    the minimum number of operations required.

    Args:
        n (int): target number of H characters

    Returns:
        int: minimum number of operations, or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
