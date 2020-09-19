# Code Kata #5 - 6 kyu
# description: You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:
# likes([]) # must be "no one likes this"
# likes(["Peter"]) # must be "Peter likes this"
# likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
# likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
# likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
# For 4 or more names, the number in `and 2 others` simply increases.

# My Solution:
def likes(names):
    listlength = len(names)
    text = ""
    if (listlength == 0):
        text = "no one likes this"
    elif (listlength == 1):
        text = f"{names[0]} like this"
    elif (listlength == 2):
        text = f"{names[0]} and {names[1]} like this"
    elif (listlength == 3):
        text = f"{names[0]}, {names[1]}, and {names[2]} like this"
    else:
        text = f"{names[0]}, {names[1]}, and {listlength-2} others like this"

    return(text)


# Top Solution:
def likes1(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


# print(likes(["juan", "tomas"]))
print(likes(["juan", "tomas", "diana", "jose"]))

# What I learned:
#   * String literals Literal String Interpolation.
#   * Using dictionary mapping as switch
#   * The min() function
