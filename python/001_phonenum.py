# Code Kata #1 - 6 kyu
# description : Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
# example : create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# My Solution
def create_phone_number(n):
    phonenum = "("
    counter = 0
    for i in n:
        if (counter == 0):
            phonenum += str(i)
        if (counter > 0 and counter < 3):
            phonenum += str(i)
        if (counter == 3):
            phonenum += ") " + str(i)
        if (counter > 3 and counter < 6):
            phonenum += str(i)
        if (counter == 6):
            phonenum += "-" + str(i)
        if (counter > 6 and counter < 10):
            phonenum += str(i)

        counter += 1

    return phonenum


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


# Top Solution - using str.format()
def create_phone_number1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


create_phone_number1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


# Solution with enumerate()
def create_phone_number2(n):
    phone = ""
    for index, c in enumerate(n):
        if index == 0:
            phone += "("
        elif index == 3:
            phone += ") "
        elif index == 6:
            phone += "-"
        phone += str(c)
    print(phone)


create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# Things learned:
# str.format to enter values inside a string,
# enumerate() to iterate without needing to use a counter variable.
