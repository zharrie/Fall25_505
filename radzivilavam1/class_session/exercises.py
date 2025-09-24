###############################################################
# Practice Problems
###############################################################
# 1. Write a for loop that prints all the even numbers from 2 to 20.
# 2. Write a while loop that calculates the sum of all integers from 1 to 100.
# 3. Write a for loop that iterates over a string and prints each character on a new line.

for number in range(2, 21, 2):
    print(number)

sum1 = 0
count = 0
while count <= 100:
    sum1 += count
    count += 1

print(sum1)

for char in "Hello, World!":
    print(char)
