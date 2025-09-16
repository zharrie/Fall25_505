# Loops
"""
A loop is a program construct that repeatedly executes the loop's statements (known as the loop body) while the loop's expression is true; when the expression is false, execution proceeds past the loop. Each time through a loop's statements is called an iteration.
Loops are used to perform repetitive tasks without having to write the same code over and over again. They can iterate over a sequence (like a list, tuple, or string) or execute a block of code a specific number of times.
There are two main types of loops in Python:
1. For Loop: Used for iterating over a sequence (like a list, tuple, dictionary, set, or string). A for loop statement iterates over each element in a container one at a time, assigning a variable to the next element to use in the loop body. 
Each iteration updates the variable with the next element. The container is typically a list, string, or dictionary. A for loop is made of a for statement, followed by an indented loop body.
for variable in container:
    # Loop body: Statements to execute
    # for each item in the container

# Statements to execute after the for loop is complete

2. While Loop: A while loop runs a block of code repeatedly as long as the while loop's condition is True. If the while loop's condition is False, then the while loop ends. Ex: A guessing game is played until a player guesses the correct answer.

while expression:  # Loop expression
    # Loop body: Statements to execute
    # if the loop expression evaluates to True

# Statements to execute after the expression evaluates to False

A sentinel value is a value that causes a loop to end. 
Ex: A while loop runs until a user inputs the sentinel value "stop", causing the loop to terminate. 
The user controls when the loop ends, thus distinguishing a loop with a sentinel value from other loops.

An infinite loop is a loop that never stops running because the loop's condition is always True. Ex: A loop that repeatedly prints a message without any condition to stop.
A common error is to accidentally create an infinite loop by assuming equality will be reached. Good practice is to include greater than or less than along with equality in a loop expression to help avoid unintended infinite loops.
An infinite loop can be valid in some programs. Ex: An infinite loop in a game checks for user input in real-time.
"""
# For Loop Example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)        

# While Loop Example
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count to avoid infinite loop
# Nested Loop Example
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# Loop with Break and Continue
for num in range(10):
    if num == 5:
        break  # Exit the loop when num is 5
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)  # This will print only odd numbers less than 5

# Loop with Else
for num in range(5):
    print(num)
else:
    print("Loop completed without break.")  

"""
Counting with a while loop

Counting is a common task in programming, often done using a loop. A loop variable can be used for counting and is updated during each iteration until the loop condition is False. Ex: If a while loop iterates 10 times, the loop variable can output values from 1 to 10 when incremented inside the loop body to count the iterations.

A common error is to forget to update the loop variable at the end of the loop (Ex:  loop_variable = loop_variable + 1), causing an unintended infinite loop.
"""
# Counting Example
count = 1  # Initialize loop variable
while count <= 10:  # Loop condition
    print(count)  # Output the current count
    count += 1  # Update loop variable to avoid infinite loop       

"""
Other compound operators
variation += 5 increments variation by 5 (that is, variation = variation + 5).
variation *= 5 multiplies variation by 5 (that is, variation = variation * 5).
variation /= 5 divides variation by 5 (that is, variation = variation / 5).
When changing how the loop variable is updated, the variable's initialization and the loop condition may also need to be adjusted for the loop to start, count, and end as expected.
"""
# Other Compound Operators Example
count = 1  # Initialize loop variable
while count <= 100:  # Loop condition
    print(count)  # Output the current count
    count *= 2  # Update loop variable using multiplication compound operator   

"""
Applications of counting with a while loop

Counting with a while loop has applications for mathematics and sequence calculations. Ex: A loop variable can be used when programming the following:

N factorial (N!) is the product of all positive integers less than or equal to N (that is, N! = N * (N - 1) * (N - 2) * . . .* 1).
The Fibonacci sequence starts with 0 or 1, and each subsequent integer is the sum of the two preceding integers.
A savings interest program can calculate the yearly savings with interest (Ex:  savings += (savings * interest_rate)).
"""
# Factorial Example
N = 5  # Number to calculate factorial for
factorial = 1  # Initialize factorial result
count = 1  # Initialize loop variable
while count <= N:  # Loop condition
    factorial *= count  # Update factorial result
    count += 1  # Update loop variable
print(f"The factorial of {N} is {factorial}")  # Output the factorial result

# Fibonacci Example
n_terms = 10  # Number of terms in the Fibonacci sequence
a, b = 0, 1  # Initialize first two terms
count = 0  # Initialize loop variable
while count < n_terms:  # Loop condition
    print(a)  # Output the current term
    a, b = b, a + b  # Update to the next two terms
    count += 1  # Update loop variable  
# Savings Interest Example
savings = 1000  # Initial savings amount
interest_rate = 0.05  # Annual interest rate
years = 10  # Number of years to calculate
count = 0  # Initialize loop variable
while count < years:  # Loop condition
    savings += (savings * interest_rate)  # Update savings with interest
    count += 1  # Update loop variable
print(f"Savings after {years} years: ${savings:.2f}")  # Output the savings result  

"""
A for loop can iterate over other containers such as strings and dictionaries. A string is a sequence type like a list, so the behavior of the loop is identical. Each iteration assigns the loop variable with the next character in the string. Ex: A for loop iterates over each character in the string "blue" beginning with "b" as the leftmost character, then each following character in the string.

Iterating over a dictionary using a for loop assigns the loop variable with each key in the dictionary in the order the keys were inserted. The key's value can then be accessed using the key.
For loops can be used to perform action during each loop iteration. A simple example is printing the value. 
A for loop may also iterate backward over a sequence, starting at the last element and ending with the first element, by using the reversed() function to reverse the order of the elements.

"""
# String Iteration Example
color = "blue"  # String to iterate over
for char in color:  # For loop iterating over each character in the string
    print(char)  # Output the current character 

# Dictionary Iteration Example
person = {"name": "Alice", "age": 30, "city": "New York"}  # Dictionary to iterate over
for key in person:  # For loop iterating over each key in the dictionary
    print(f"{key}: {person[key]}")  # Output the key and its corresponding value

# Reverse Iteration Example
numbers = [1, 2, 3, 4, 5]  # List to iterate over in reverse
for num in reversed(numbers):  # For loop iterating over the list in reverse order
    print(num)  # Output the current number

"""
The range() function

While loops are often used for counting a specific number of iterations, and for loops are often used to iterate over all elements of a container. The range() function allows counting in for loops as well. range() generates a sequence of integers between a starting integer that is included in the range, an ending integer that is not included in the range, and an integer step value. The sequence is generated by starting at the start integer and incrementing by the step value until the ending integer is reached or surpassed.

The range() function can take up to three integer arguments.

range(Y) generates a sequence of all non-negative integers less than Y.
Ex: range(3) creates the sequence 0, 1, 2.
range(X, Y) generates a sequence of all integers >= X and < Y.
Ex: range(-7, -3) creates the sequence -7, -6, -5, -4.
range(X, Y, Z), where Z is positive, generates a sequence of all integers >= X and < Y, incrementing by Z.
Ex: range(0, 50, 10) creates the sequence 0, 10, 20, 30, 40.
range(X, Y, Z), where Z is negative, generates a sequence of all integers <= X and > Y, incrementing by Z.
Ex: range(3, -1, -1) creates the sequence 3, 2, 1, 0.

Range	        Generated sequence	Explanation
range(5)	        0 1 2 3 4       Every integer from 0 to 4
range(0, 5)	        0 1 2 3 4       Every integer from 0 to 4
range(3, 7)	        3 4 5 6         Every integer from 3 to 6
range(10, 13)	    10 11 12        Every integer from 10 to 12
range(0, 5, 1)	    0 1 2 3 4       Every 1 integer from 0 to 4
range(0, 5, 2)	    0 2 4           Every 2nd integer from 0 to 4
range(5, 0, -1)	    5 4 3 2 1       Every 1 integer from 5 to 1
range(5, 0, -2)	    5 3 1           Every 2nd integer from 5 to 1

Evaluating the range() function creates a new "range" type object. 
Ranges represent an arithmetic progression, i.e., some sequence of integers with a start, end, and step between integers. 
The range type is a sequence type like lists and tuples but is immutable. In general, range objects are only used as part of a for loop statement.
"""
# Range Function Example
for i in range(5):  # For loop iterating over range from 0 to 4
    print(i)  # Output the current integer in the range

for i in range(3, 7):  # For loop iterating over range from 3 to 6
    print(i)  # Output the current integer in the range

for i in range(0, 10, 2):  # For loop iterating over range from 0 to 9 with step of 2
    print(i)  # Output the current integer in the range

for i in range(5, 0, -1):  # For loop iterating over range from 5 to 1 with step of -1
    print(i)  # Output the current integer in the range 

# The remaining topics will be covered on Thursday