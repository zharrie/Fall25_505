"""
Write a program that takes an integer (0 - 9999) as input and outputs the number of digits.

Ex: If the input is:

7493
the output is:

4 digits
Ex: If the input is:

7
the output is:

1 digit



"""

value = input()
my_list = value.split()
# print(my_list)
i = 0
for v in my_list:
    i += 1
print(i)   
