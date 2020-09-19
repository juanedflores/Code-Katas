# Code Kata #5 - 6 kyu
# Trolls are attacking your comment section! A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat. Your task is to write a function that takes a string and return a new string with all vowels removed. For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!". Note: for this kata y isn't considered a vowel.

# My Solution:
import re


def disemvowel(string):
    s = ""
    for l in string:
        if (l not in "aeiouAEIOU"):
            s += l
    return(s)


# Top Solution:
def disemvowel1(string):
    return string.translate(None, "aeiouAEIOU")


# Solution with join() and lower()
def disemvowel2(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


# Solution with replace()
def disemvowel3(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, '')
    return s


# Solution with regular expressions and IGNORECASE flag
def disemvowel4(string):
    return re.sub('[aeiou]', '', string, flags=re.IGNORECASE)


print(disemvowel("LOLwhatisgoingon"))

# What I learned:
#   * translate() function
#   * Remembered that the string.lower() and string.upper() functions exist.
#   * the replace() function
#   * the regular expression module
