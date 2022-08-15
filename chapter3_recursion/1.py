# Chapter 3 Exercise 1 Fibonacci

# a
def fib_rec(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # fib definition
    return fib_rec(n - 1) + fib_rec(n - 2)

# b
def fib_it(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1

    for _ in range(1, n):
        a, b = b, a + b

    return b

for i in range(0, 9):
    print('{i} rec: {v}'.format(i=i, v=fib_rec(i)))
    print('{i} it: {v}'.format(i=i, v=fib_it(i)))
