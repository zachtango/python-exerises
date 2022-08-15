# Chapter 3 Exercise 8 Exponential Function

# a
def is_power_of_2(n: int) -> bool:
    if n <= 2:
        return n == 2
    elif n % 2 == 1:
        return False

    return is_power_of_2(n // 2)

# b
def power_of(value: int, exponent: int) -> int:
    if exponent == 0:
        return 1

    return value * power_of(value, exponent - 1)

def power_of_fast(value: int, exponent: int) -> int:
    if exponent == 0:
        return 1

    new_exponent = exponent // 2
    if exponent % 2 == 0:
        return power_of_fast(value, new_exponent) * power_of_fast(value, new_exponent)
    else:
        return value * power_of_fast(value, new_exponent)

# c
def power_of_it(value: int, exponent: int) -> int:
    accum = 1

    for _ in range(0, exponent):
        accum *= value

    return accum

def power_of_it_fast(value: int, exponent: int) -> int:

    accum = 1
    b = value

    while exponent != 0:
        if exponent % 2 == 1:
            accum *= b
        b = b * b

        exponent //= 2


    return accum

tests = [
    (2, 2),
    (10, 8),
    (16, 4)
]

for test in tests:
    print(test)
    print(is_power_of_2(test[0]))
    print(power_of(test[0], test[1]))
    print(power_of_fast(test[0], test[1]))
    print(power_of_it(test[0], test[1]))
    print(power_of_it_fast(test[0], test[1]))

