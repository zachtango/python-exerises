# Chapter 3 Exercise 3 GCD

# a
'''
Write function gcd(a, b) that computes the greatest common divisor (GCD)
'''

def gcd_rec(a: int, b: int):
    if b > a:
        return gcd_rec(b, a)
    
    if b == 0:
        return a

    return gcd_rec(b, a % b)

# b
def gcd_it(a: int, b: int):
    if b > a:
        return gcd_it(b, a)
    
    while b != 0:
        a, b = b, a % b
    
    return a


# c
'''
Write function lcm(a, b) that computes the least common multiplier (LCM).
'''
def lcm(a: int, b: int):
    return (a * b) // gcd_it(a, b)

tests = [
    (42, 7),
    (42, 28),
    (42, 14)
]

for test in tests:
    print(test)
    print(gcd_rec(*test))
    print(gcd_it(*test))
    print(lcm(*test))