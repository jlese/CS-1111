# Date: Feb 4, 2019
#
# write function
# return vs. print
# input()
# casting: int()
# expression: % and **
# function with parameters, calling with arguments

#################################

# Write a function that takes 2 numbers (named n1 and n2) and
# returns whether n1 is evenly divisible by n2
# 4 % 2 give remainder

def is_divisible(n1, n2):
    return n1 % n2 == 0


print(is_divisible(4, 2))  # expected output True
print(is_divisible(3, 2))  # expected output False
print(is_divisible(5, 3))  # expected output False
print(is_divisible(9, 3))  # expected output True


# Modify the is_divisible() function (above) to
# get 2 numbers from a keyboard.
# That is, instead of passing n1 and n2 as arguments,
# use input() to get the numbers

def is_divisible2():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))

    return n1 % n2 == 0


print(is_divisible2())
print(is_divisible2())
print(is_divisible2())
print(is_divisible2())


#################################

# Write a function that takes 2 numbers (named n1 and n2) and
# returns n1 to the power n2 ( n1 ** n2)

def power(n1, n2):
    return n1 ** n2


print(power(4, 2))  # expected output 16
print(power(3, 2))  # expected output 9
print(power(5, 3))  # expected output 125
print(power(9, 3))  # expected output 729
print(power(26, 0))  # expected output 1
print(power(4, 1.2))  # expected output 5.278031643091577


#################################

# Write a function that gets the radius of a circle,
# and displays and returns
# the approximation of the circle's area.
# Use 3.14 as the value for pi.

def compute_area(radius):
    return 3.14 * (radius ** 2)


print(compute_area(3))  # 28.26



#################################

# Write a function that takes a number,
# and returns a sum of the next three multiples of that number
# multiplied by three
#
# For example, if the input is the number 2,
# the function would return 78 which is
# a sum of "6 18 54". (54 is 3 times 18)

def template(number1):




print(template(0))  # expected output 0
print(template(1))  # expected output 39
print(template(2))  # expected output 78


#################################

# Write a function that a number,
# and returns a string containing the next three multiples
# of that number multiplied by three, separated by spaces.
#
# For example, if the input is the number 2,
# the function would return the string
# "6 18 54". (54 is 3 times 18)

def template2(number1):
    pass


print(template2(0))  # expected output '0 0 0'
print(template2(1))  # expected output '3 9 27'
print(template2(2))  # expected output '6 18 54'


#################################

# Write a function that takes a one to three-digit integer,
# and adds together all of its digits. For example, 123
# would return 6.
# Hint: remember you can use division and modulus operators

def sumdigits(number1):
    pass


print(sumdigits(23))  # expected output 5
print(sumdigits(203))  # expected output 5
print(sumdigits(230))  # expected output 5
print(sumdigits(0))  # expected output 0
print(sumdigits(123))  # expected output 6


#################################

# Write a function that gets 5 numbers,
# computes and returns the following:
#   1. sum of the numbers
#   2. average of the numbers

def compute_basic_math(n1, n2, n3, n4, n5):
    pass


print(compute_basic_math(5, 3, 2, 6, 2))  # expected output (18, 3.6)

#################################

# consider
# 1. where the functions are defined
# 2. where the functions are called
# 3. flow of the function calls
