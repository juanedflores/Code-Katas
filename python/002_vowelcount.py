# Code Kata #2 - 7 kyu
# description : Return the number (count) of vowels in the given string.
# We will consider [a, e, i, o, u] as vowels, not [y].
# The input string will only consist of lower case letters and/or spaces.

# My Solution
def get_count(inputStr):
    num_vowels = 0
    vowels = "aeiou"

    for letter in inputStr:
        if (letter in vowels):
            num_vowels += 1

    return num_vowels


# Top Solution
def get_count1(inputStr):
    return sum(1 for letter in inputStr if letter in "aeiouAEIOU")
# This works because it is using a generator object that returns 1 if any letter
# matches any of the vowels in the string.
# If you break it down to this:
# gen = 1 for let in inputStr if let in "aeiouAEIOU"
# for i in gen:
#   print(i)
# the result will be five ones.
# Passing in this generator object to the sum function simply adds up all of these ones to get the final result.


print(get_count("abracadabra"))

# What I learned:
# How to use the 'in' keyword with an if statement to check if a char matches any chars of a given string.
# Using the sum() function.
# Using generator functions.
# list comprehensions and generator comprehensions
