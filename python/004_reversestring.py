# Code Kata #4 - 8 kyu
# description: Complete the solution so that it
# reverses the string passed into it.
# example: 'world'  =>  'dlrow'

# My Solution
def solution(string):
    return string[::-1]


# Solution with anonymous function
# and that is a one liner
def solution1(s): return s[::-1]


# Solution using reverse method
def solution2(string):
    temp = list(string)
    temp.reverse()
    return ''.join(temp)


print(solution2("world"))

# What I learned:
# * The pass keyword, as a placeholder for future code.
# * How reverse() or [::-1] works on the surface:
#       for char in range(len(string)-1, -1, -1):
#           return string[char]
