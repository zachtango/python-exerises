# Chapter 3 Exercise 9 Pascal's Triangle

def pascal_rec(row: int, col: int) -> int:
    if col == 1 or col == row:
        return 1

    return pascal_rec(row - 1, col - 1) + pascal_rec(row - 1, col)

def print_pascal(n: int) -> None:
    for r in range(1, n + 1):
        s = '['
        for c in range(1, r + 1):
            s += ' {v}'.format(v=pascal_rec(r, c))
        s += ']'

        print(s)

print_pascal(5)
    