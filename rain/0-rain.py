#!/usr/bin/python3
"""
0-rain
"""


def rain(walls):
    """Calculate how much water is retained between walls.

    walls is a list of non-negative integers representing wall heights.
    Return the total amount of rainwater that can be retained.
    """
    if not walls:
        return 0

    size = len(walls)
    left = [0] * size
    right = [0] * size

    max_left = 0
    for i in range(size):
        left[i] = max_left
        if walls[i] > max_left:
            max_left = walls[i]

    max_right = 0
    for i in range(size - 1, -1, -1):
        right[i] = max_right
        if walls[i] > max_right:
            max_right = walls[i]

    total = 0
    for i in range(size):
        limit = min(left[i], right[i])
        if limit > walls[i]:
            total += limit - walls[i]

    return total
