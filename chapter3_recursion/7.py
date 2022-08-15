# Chapter 3 Exercise 7 Conversions


# a
def to_binary(n: int) -> str:
    if n == 0:
        return ''

    return to_binary(n // 2) + str(n % 2)

# b
def to_octal(n: int) -> str:
    if n == 0:
        return ''

    return to_octal(n // 8) + str(n % 8)

hex = {d: str(d) for d in range(0, 10)}
hex[10], hex[11], hex[12], hex[13], hex[14], hex[15] = 'A', 'B', 'C', 'D', 'E', 'F'

def to_hex(n: int) -> str:
    if n == 0:
        return ''
    
    return to_hex(n // 16) + hex[n % 16]
    
bin_tests = [5, 7, 22, 42, 256]
oct_hex_tests = [7, 8, 42, 15, 77]

for t in bin_tests:
    print(to_binary(t))

for t in oct_hex_tests:
    print(to_octal(t))
    print(to_hex(t))
