###############################################################
# Practice Problems
###############################################################
# 1. Write a for loop that prints all the even numbers from 2 to 20.
# 2. Write a while loop that calculates the sum of all integers from 1 to 100.
# 3. Write a for loop that iterates over a string and prints each character on a new line.

for i in range(2, 21, 2):
    print(i)

total_sum = 0
num = 1
while num <= 100:
    total_sum += num
    num += 1
print(total_sum)

text = "Good Morning"
for char in text:
    print(char)