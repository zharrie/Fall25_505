#Write a program whose inputs are four integers, and whose outputs are the maximum and the minimum of the four values.

#Ex: If the input is:

#12
#18
#4
#9
#the output is:

#Maximum is 18 
#Minimum is 4
#The program must define and call the following two functions.
# Define a function named max_number() that takes four integer parameters and returns an integer 
#representing the maximum of the four integers. Define a function named min_number() that takes 
#four integer parameters and returns an integer representing the minimum of the four integers.
#def max_number(num1, num2, num3, num4)
#def min_number(num1, num2, num3, num4)

#Note: DO NOT use max() and min().

# My Explanation: first we will need to read the input values(a,b,c,d).
a=int(input())
b=int(input())
c=int(input())
d=int(input())
# Then we will define the function max_number to find the maximum value among the four inputs.
def max_number(a, b, c, d):
    # now the first number will be the maximum
    maximum = a
    # I will create if func to compare with the other numbers
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    if d > maximum:
        maximum = d
    return maximum
# now I will do the same for the minimum func.
def min_number(a, b, c, d):
    minimum = a
    if b< minimum:
        minimum = b
    if c < minimum:
        minimum = c
    if d< minimum:
        minimum = d
    return minimum
# create two print functions one for max and one for min.
print(f"Maximum is {max_number(a, b, c, d)}")
print(f"Minimum is {min_number(a, b, c, d)}")  