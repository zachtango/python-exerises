# Chapter 3 Exercise 5 List Sum

def sum_rec(values: list[int]) -> int:
    if not values:
        return 0

    return values[0] + sum_rec(values[1:])

tests = [
    [1, 2, 3],
    [1, 2, 3, -7]
]

for test in tests:
    print(sum_rec(test))