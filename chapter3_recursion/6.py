# Chapter 3 Exercise 6 List Min

import sys


def min_rec(values: list[int]) -> int:
    if not values:
        return sys.maxsize
    
    if values[0] < min_rec(values[1:]):
        return values[0]
    
    return min_rec(values[1:])

tests = [
    [7, 2, 1, 9, 7, 1],
    [11, 2, 33, 44, 55, 6, 7],
    [1, 2, 3, -7]
]

for test in tests:
    print(min_rec(test))