# Code Kata #3 - 7 kyu
# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# The binary number returned should be a string.

import math


# My Solution
# Note: After I realized that there is no need
# to use math.floor() after using floor division.
def add_binary(a, b):
    decsum = a + b

    rem = math.floor(decsum % 2)
    decimal = math.floor(decsum // 2)
    binary = [rem]
    while decimal > 2:
        rem = math.floor(decimal % 2)
        decimal = math.floor(decimal // 2)
        binary.append(rem)

    if (decimal == 1):
        binary.append(1)
    elif(decimal == 2):
        binary.append(10)

    # convert reversed array to string
    result = ""
    for i in binary[::-1]:
        result += str(i)

    return(result)


# Top Solution - using the bin() function.
def add_binary1(a, b):
    return bin(a+b)[2:]


# Using foratting to convert to binary.
def add_binary2(a, b):
    return "{0:b}".format(a + b)


# Another way to use format() to convert to binary.
def add_binary3(a, b):
    return format(a + b, 'b')


# Solution without using the built-in conversion methods.
def find_highest_power_2(num):
    n = 0
    # a user suggests using 1 << n instead of 2 ** n, because it is faster.
    while 2**n <= num:
        n += 1
        print(1 << n)
    return n-1


def add_binary4(a, b):
    sum = a + b
    number = 0
    while sum != 0:
        place_holder = find_highest_power_2(sum)
        number += 10**place_holder
        sum = sum - 2**place_holder
    return str(number)


print(add_binary(40, 60))

# What I learned:
# * How to convert decimal to binary.
# * the // operator - to divide large numbers, to get ints.
# * reversing a list by slicing [::-1]
# * appending to a list using list.append()
# * Using the math module to use floor() or ceil()
# * The bin() function to convert to binary.
# * Using formatting to convert to binary.
# * bitwise operators
