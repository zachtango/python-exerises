# Chapter 3 Exerise 2 Process Digits

# a
'''
    Write recursive function count_digits(value) that finds the number of digits in a positive natural number. 
'''
def count_digits(value: int):
    if value == 0:
        return 1

    return 1 + count_digits(value // 10)

# b
'''
    Calculate the sum of the digits of a number recursively. Write recursive function calc_sum_of_digits(value) for this purpose.
'''
def calc_sum_of_digits(value: int):
    if value == 0:
        return 0
    
    digit = value % 10

    return digit + calc_sum_of_digits(value // 10)

print('number of digits: ' + str(count_digits(1234567)))
print('cross sum: ' + str(calc_sum_of_digits(1234567)))
