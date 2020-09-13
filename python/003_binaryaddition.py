# Code Kata #3 - 7 kyu
# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# The binary number returned should be a string.

import math


# My Solution
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


print(add_binary1(4, 6))

# What I learned:
# * How to convert decimal to binary.
# * the // operator - to divide large numbers, to get ints.
# * reversing a list by slicing [::-1]
# * appending to a list using list.append()
# * Using the math library and using floor() or ceil()
# * The bin() function to convert to binary.
