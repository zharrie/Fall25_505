# 1- Basic File Reading: Create a text file with several lines of text. Write a program that reads and prints each line with line numbers.
#Open the file in read mode
with open("example.txt", "r") as file:
#Read all lines into a list
    lines = file.readlines()

#Loop through the lines and print with line numbers
for index, line in enumerate(lines, start=1):
    print(index, line)


# 2- Data Processing: Create a file with numbers (one per line). Write a program that calculates and prints the average.
# Open the file in read mode
with open("numbers.csv", "r") as file:
    numbers = file.readlines()

# Create an empty list to store the numbers
numbers_list = []

#Go through each line in the file
for num in numbers:
#Remove any spaces or newline characters and convert to a float
    number = float(num.strip())
#Add the number to the list
    numbers_list.append(number)

#Calculate the average
if numbers: 
    average = sum(numbers_list) / len(numbers)
    print(f"Average: {average}")
else:
    print("The file is empty.")
#
# 3- File Copying: Write a program that copies the contents of one file to another using the with statement.

# 4- CSV Analysis: Create a CSV file with student grades. Write a program that calculates each student's average and writes the results to a new CSV file.

# 5- Directory Search: Use os.walk() to find all .txt files in a directory tree and print their full paths.

