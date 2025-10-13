"""Write a program whose inputs are four integers, 
and whose outputs are the maximum and the minimum of the four values.

Ex: If the input is:

12
18
4
9
the output is:

Maximum is 18 
Minimum is 4
The program must define and call the following two functions.
 Define a function named max_number() that takes four integer parameters and returns an integer representing the maximum of the four integers. 
 Define a function named min_number() that takes four integer parameters and returns an integer representing the minimum of the four integers.

def max_number(num1, num2, num3, num4)
def min_number(num1, num2, num3, num4)

Note: DO NOT use max() and min()."""


def max_number(num1, num2, num3, num4):
    max_list = []
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    max_list = max_list.append(num1, num2, num3, num4)
    max_list = sorted(max_list)
    max_num = max_list[-1] 
    return max_num 



def min_number(num1, num2, num3, num4):
    min_list = []
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    min_list = min_list.append(num1, num2, num3, num4)
    min_list = min_list.sorted
    min_num = min_list[0]
    return min_num

max_number()
print(f"Maximum is {max_num}")

min_number()
print(f"Minimum is {min_num}")