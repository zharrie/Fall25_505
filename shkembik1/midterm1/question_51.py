#Write a program that takes an integer (0 - 9999) as input and outputs the number of digits.

#Ex: If the input is:

#7493
#the output is:

#4 digits
#Ex: If the input is:

#7
#the output is:

#1 digit
# My Explanation: first we will need to read the input.
# then we will create if else func to check how many digits the number has.
# the idea is that the number can be 1, 2, 3 or 4 digits. 
# numbers with 1 digit are from 0 to 9
# numbers with 2 digits are from 10 to 99
# numbers with 3 digits are from 100 to 999
# numbers with 4 digits are from 1000 to 9999

a=int(input())
if a<10:
    print("1 digit")
elif a<100:
    print("2 digits")
elif a<1000:
    print("3 digits")
else:             
    print("4 digits")

   







