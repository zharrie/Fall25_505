# Write a program whose inputs are four integers, and whose outputs are the maximum and the minimum of the four values.

# Ex: If the input is:

# 12
# 18
# 4
# 9
# the output is:

# Maximum is 18 
# Minimum is 4
# The program must define and call the following two functions. Define a function named max_number() that takes four integer parameters and returns an integer representing the maximum of the four integers. Define a function named min_number() that takes four integer parameters and returns an integer representing the minimum of the four integers.

# def max_number(num1, num2, num3, num4)
# def min_number(num1, num2, num3, num4)

# Note: DO NOT use max() and min().



# MY COMMENTS


# numbers = input()
# numbers_list_string = numbers.split()
# numbers_list_int = []
# for i in numbers_list_string:
#     i = int(i)
#     numbers_list_int.append(i)

# First we need to get user input which will be a string since it's a few different numbers.
#Then we need to convert if to intergers and we can keep them in a list for future use with functions

input1 = int(input())
input2 = int(input())
input3 = int(input())
input4 = int(input())

#Alternatevrly we can just ask for 4 integers separatly, which will be easier.

def max_number(int1, int2, int3, int4):
    highest = int1
    if highest < int2:
        highest = int2
    if highest < int3:
        highest = int3
    if highest < int4:
        highest = int4
    return highest

# In this function I want to see if the first number is higher than the second one.
# If it is it assigns the variable highest with the higher number and if not - it will compare the first number with the third number.
#It will work because I'm using multiple "ifs" instead of if-else statements


def min_number(int1, int2, int3, int4):
    lowest = int1
    if lowest > int2:
        lowest = int2
    if lowest > int3:
        lowest = int3
    if lowest > int4:
        lowest = int4
    return lowest
#It's the same logic as with the max_number function - just in reverse

print ("Maximum is", max_number(input1, input2, input3, input4))
print ("Minimum is", min_number(input1, input2, input3, input4))