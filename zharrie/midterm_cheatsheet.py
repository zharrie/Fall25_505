# Midterm Prep for hands on coding problems
"""
1. Program: Grade calculator

Write a program to calculate a course grade given points for homework, quizzes, midterm exam, and final exam. 
Grades are calculated differently for undergrads, grads and distance learners.

Note: this program is designed for incremental development. Complete each step before starting the next step. 

Step 1 (2 pts). 
Read from input student status (str). 
If input is not one of "UG" (undergrad), "G" (grad), or "DL" (distance learner), print an error message and exit the program. 
Otherwise read from input floats for homework points, quiz points, midterm exam score, and final exam score. 
Calculate each category's average using maximum points for homework (800), quizzes (400), midterm exam (150), and final exam (200). 
Output category averages as a percentage using print(f"Homework: {homework:2.1f}%"). 

Ex: If the input is:
UG
600.0  300.0  120.0  185.0

The output is:
Homework: 75.0%
Quizzes: 75.0%
Midterm: 80.0%
Final Exam: 92.5%

Step 2 (2 pts). 
Set any average to 100% if average is above 100%. Submit for grading to confirm three tests pass.
Ex: If the input is:
UG
700.0  300.0  200.0  205.0
The output is:
Homework: 87.5%
Quizzes: 75.0%
Midterm: 100.0%
Final Exam: 100.0%

Step 3 (2 pts). 
Calculate the course average based on student status using the table below. 
Output the course average. 

Category	    UG	    G	    DL
Homework	    20%	    15%	    5%
Quizzes	        20%	    5%	    5%
Midterm	        30%	    35%	    40%
Final Exam	    30%	    45%	    50%

Ex: If the input is:
G
800.0   400.0   100.0   100.0

The output is:
Homework: 100.0%
Quizzes: 100.0%
Midterm: 66.7%
Final Exam: 50.0%
G average: 65.8%

Step 4 (4 pts). 
Identify the course letter grade based on the course average using the table below. 
Output the course letter grade. 


Average	                            Grade
at least 90.0	                    A
at least 80.0 and less than 90.0	B
at least 70.0 and less than 80.0	C
at least 60.0 and less than 70.0	D
less than 60.0	                    F

Ex: If the input is:
DL
600.0  300.0  120.0  150.0

The output is:
Homework: 75.0%
Quizzes: 75.0%
Midterm: 80.0%
Final Exam: 75.0%
DL average: 77.0%
Course grade: C
"""

"""
2. Count multiples
Write a program that takes three integers as input: low, high, and x. 
The program then outputs the number of multiples of x between low and high exclusive.
Ex: If the input is:
1
10
2
the output is:
Multiples of 2: 2,4,6,8,
For coding simplicity, follow each output number by a comma, even the last one.

Hint: Use the % operator to determine if a number is a multiple of x. Use a for loop to test each number between low and high.
"""

"""
3. Toll calculation
Toll roads have different fees based on the time of day and on weekends. 
Write a function calc_toll() that has three parameters: the current hour of time (int), whether the time is morning (boolean), and whether the day is a weekend (boolean). 
The function returns the correct toll fee (float), based on the chart below.

Weekday Tolls

Before 7:00 am ($6.15)
7:00 am to 9:59 am ($7.95)
10:00 am to 2:59 pm ($6.90)
3:00 pm to 7:59 pm ($8.95)
Starting 8:00 pm ($6.40)
Weekend Tolls

Before 7:00 am ($6.05)
7:00 am to 7:59 pm ($7.15)
Starting 8:00 pm ($6.10)
Ex: The function calls below, with the given arguments, will return the following toll fees:

calc_toll(8, True, False) returns 7.95
calc_toll(1, False, False) returns 6.90
calc_toll(3, False, True) returns 7.15
calc_toll(5, True, True) returns 6.05
"""

"""
4. Remove digits - functions
Write a program that removes all digits from the given input.

Ex: If the input is:
1244Crescent
the output is:
Crescent

The program must define and call the following function that takes a string as parameter and returns the string without any digits.

def remove_digits(user_string)
"""

"""
5. List palindrome
Write a program that reads a list of integers from input and determines if the list is a palindrome (values are identical from first to last and last to first). The input begins with an integer indicating the length of the list that follows. Assume that the list will always contain fewer than 20 integers. Output "yes" if the list is a palindrome and "no" otherwise. The output ends with a newline.

Ex: If the input is:
6 
1
5
9
9
5
1
the output is:
yes

Ex: If the input is:
5 
1 
2
3
4
5
the output is:
no
"""

"""
6. Matrix multiplication
A matrix is a rectangle of numbers in rows and columns. A 1xN matrix has one row and N columns. An NxN matrix has N rows and N columns.

Multiplying a 1xN matrix A and an NxN matrix B produces a 1xN matrix C. To determine the Nth element of C multiply the each element of A by each element of the Nth column of B and sum the results. Helpful information can be found at matrix multiplication.

Write a program that reads a 1xN matrix A and an NxN matrix B from input and outputs the 1xN matrix product, C. N can be of any size >= 2.

A is represented as a list of the integers found on the first line of input.
B is represented as a list of N rows, each of which is a list of N integers.
Each of the next N input lines contains the integers for one row of B.
Note: Input is one row at a time but multiplication uses columns of B.
For coding simplicity, follow each output integer by a space, even the last one. The output ends with a newline.

Ex: If the input is:
2 3
1 2
3 4

A contains 2 and 3, the first row of B contains 1 and 2, and the second row of B contains 3 and 4. The first element of C is (2 * 1) + (3 * 3), and the second element of C is (2 * 2) + (3 * 4). The program output is:
11 16
"""
