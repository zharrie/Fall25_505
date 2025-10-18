# When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This can be done by normalizing to values between 0 and 1, or throwing away outliers. For this program, adjust the values by subtracting each value from the maximum. Input values should be added to the list until -1 is entered.

# Ex: If the input is:

# 30
# 50
# 10
# 70
# 65
# -1
# the output is:

# 40
# 20
# 60
# 0
# 5
# Your program must define and call the function:
# def get_max_int(nums)

# Note: get_max_int() returns the maximum value in the list.

#MY COMMENTS

user_input = int(input())

my_list = []
while user_input != -1:
    my_list.append(user_input)
    user_input = int(input())

#First we get first input from a user and then get more input with the help of the while loop
#untill the user prints -1
#We put all the input into the list

def get_max_int(nums):
    highest = max(nums)
    return highest
#Then we define a function that takes a list as an argument and gives us the highest number

highest_input = get_max_int(my_list)
#We call the function and create a new variable
new_list = []
for i in my_list:
    i = highest_input - i
    new_list.append(i)


#We create a new list of integers and put new integers into new list

print(new_list)

#had no time to print with spaces

