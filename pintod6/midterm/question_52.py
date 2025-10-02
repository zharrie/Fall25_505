"""
Write a program whose inputs are four integers, and whose outputs are the maximum and the minimum of the four values.

Ex: If the input is:

12
18
4
9
the output is:

Maximum is 18 
Minimum is 4
The program must define and call the following two functions. Define a function named max_number() that takes four integer parameters and returns an integer representing the maximum of the four integers. Define a function named min_number() that takes four integer parameters and returns an integer representing the minimum of the four integers.

def max_number(num1, num2, num3, num4)
def min_number(num1, num2, num3, num4)


"""

def max_number(num, num1, num2, num3):
    temp = 0
    l = [num, num1, num2, num3]
    for value in l:
        if value > temp:
            temp = value
    print(temp)

val = max_number(1, 2, 3, 4)            
    


    