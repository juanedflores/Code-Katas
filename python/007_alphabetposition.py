# Code Kata #7 - 6 kyu
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

# My Solution:
def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for letter in text.lower():
        if letter not in alphabet.lower():
            continue
        index = alphabet.find(letter)
        output += str(index+1) + " "
    return(output[:-1])


# Top Solution:
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position("hello"))

# What I learned:
#   * str.isAlpha() function.
#   * ord() function to find the unicode code for a character.
#   * find() function to get the index of a char in the string.
#   * comprehensions
#   * you can import string and use string.ascii_lowercase to get the alphabet.
