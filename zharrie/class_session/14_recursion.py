"""
What is Recursion?
How Recursion Works: Understanding Namespaces
Recursive Algorithms Explained
Binary Search: A Classic Example
Creating Recursive Functions
Debugging Recursive Functions
Mathematical Applications
Recursion Depth and Limits
Best Practices and Common Pitfalls

Recursion occurs when a function calls itself to solve a problem. 
A function that calls itself is known as a recursive function.

Think of it like looking into two mirrors facing each other—each reflection contains another reflection, 
creating a repeating pattern that eventually fades away.

"""
# A Simple Example: Countdown

def count_down(count):
    """Count down from a number to zero"""
    if count == 0:
        print("GO!")
        return
    else:
        print(count)
        count_down(count - 1)  # The function calls itself!
count_down(3)
"""
Output:
3
2
1
GO!
"""

# Iterative version (more common for simple counting)
for i in range(3, 0, -1):
    print(i)
print("GO!")

"""
How Recursion Works: Understanding Namespaces

2.1 The Call Stack and Namespaces

Every time a function is called, Python creates a new namespace (a separate memory space) for that function's local variables. 
This is crucial to understanding how recursion works.

Let's trace through count_down(2) step by step:
"""

def count_down(count):
    if count == 0:
        print("GO!")
        return
    else:
        print(count)
        count_down(count - 1)

count_down(2)
"""
2.2 Step-by-Step Execution

Step 1: First call to count_down(2)

A namespace is created with count = 2
Since count ≠ 0, we execute the else branch
Prints 2
Calls count_down(1)
Step 2: Second call to count_down(1)

A new namespace is created with count = 1
Since count ≠ 0, we execute the else branch
Prints 1
Calls count_down(0)
Step 3: Third call to count_down(0)

A new namespace is created with count = 0
Since count == 0, we execute the if branch
Prints GO!
Returns (base case reached!)
Step 4: Unwinding

Third call returns to second call → second call completes
Second call returns to first call → first call completes
First call returns to the main script → script finishes

2.3 Visualizing the Call Stack


Main Script
    │
    └─ count_down(2)         # Namespace 1: count = 2
           │
           ├─ prints: 2
           │
           └─ count_down(1)  # Namespace 2: count = 1
                  │
                  ├─ prints: 1
                  │
                  └─ count_down(0)  # Namespace 3: count = 0
                         │
                         ├─ prints: GO!
                         │
                         └─ returns
Key Insight: Each function call has its own separate count variable that doesn't interfere with the others!
"""

"""
What is an Algorithm?

An algorithm is simply a sequence of steps for solving a problem.

Example: Non-Recursive Algorithm

Making Lemonade:


Step 1: Add sugar to pitcher
Step 2: Add lemon juice
Step 3: Add water
Step 4: Stir
Each step is distinct and executed once in order.

3.3 Example: Recursive Algorithm

Mowing the Lawn:


Mow the lawn:
    ├─ Mow the front yard
    │   ├─ Mow the left front
    │   └─ Mow the right front
    └─ Mow the backyard
        ├─ Mow the left back
        └─ Mow the right back
Notice how "mowing the lawn" is defined in terms of smaller "mowing" tasks. The algorithm calls itself on smaller regions—this is recursive thinking!

3.4 Real-World Example: The Number Guessing Game

Problem: Your friend thinks of a number between 0 and 100. You need to guess it, and they'll tell you "higher" or "lower" after each guess. How can you minimize the number of guesses?

Strategy 1: Linear Search (Inefficient)


Guess 0? Higher
Guess 1? Higher
Guess 2? Higher
...
Average guesses needed: 50
Strategy 2: Guess by Tens (Better)


Guess 10? Higher
Guess 20? Higher
Guess 30? Lower
Guess 21? Higher
Guess 22? Higher
Guess 23? Correct!
Average guesses needed: ~10
Strategy 3: Binary Search (Optimal)


Range: 0-100, Guess 50? Lower
Range: 0-50,  Guess 25? Higher
Range: 26-50, Guess 38? Lower
Range: 26-38, Guess 32? Higher
Range: 33-38, Guess 35? ...
Average guesses needed: ~7
Key Insight: After each guess, we apply the same algorithm (binary search) to a smaller range. This is perfect for recursion!

4. Binary Search: A Classic Example

4.1 The Binary Search Algorithm

Binary search repeatedly divides the search space in half:

Guess the midpoint of the range
If correct, done!
If the answer is lower, search the lower half
If the answer is higher, search the upper half
Repeat (recursion!)
4.2 Implementing Binary Search Recursively

Let's implement a function to search for an item in a sorted list:
"""

def find(names, target, low, high):
    """
    Search for target in sorted list names[low:high+1]
    Returns index if found, -1 if not found
    """
    # Calculate middle index
    mid = (low + high) // 2
    
    # BASE CASE 1: Found the target!
    if names[mid] == target:
        return mid
    
    # BASE CASE 2: Search space is empty (not found)
    if low == high:
        return -1
    
    # RECURSIVE CASE 1: Search lower half
    if target < names[mid]:
        return find(names, target, low, mid - 1)
    
    # RECURSIVE CASE 2: Search upper half
    else:
        return find(names, target, mid + 1, high)

# Example: Conference attendee list (sorted alphabetically)
attendees = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]

# Search for "Diana"
result = find(attendees, "Diana", 0, len(attendees) - 1)
print(f"Diana is at index: {result}")  # Output: Diana is at index: 3

# Search for someone not in the list
result = find(attendees, "Zoe", 0, len(attendees) - 1)
print(f"Zoe is at index: {result}")   # Output: Zoe is at index: -1


# Notice the if-else pattern that's common in recursive functions:

if base_case_condition:
    return base_value  # Stop recursion
else:
    return recursive_call(smaller_problem)  # Continue recursion

"""    
4.4 How Binary Search Reduces the Problem

Let's trace searching for "Diana" in our list:


Step 1: Search ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
        low=0, high=6, mid=3
        names[3] = "Diana" ✓ Found!
Let's trace searching for "Frank":


Step 1: Search ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
        low=0, high=6, mid=3
        names[3] = "Diana" < "Frank"
        → Search upper half

Step 2: Search ["Eve", "Frank", "Grace"]
        low=4, high=6, mid=5
        names[5] = "Frank" ✓ Found!
Key Point: Each step reduces the problem to a smaller, identical problem—perfect for recursion!

4.5 Recursion vs. Iteration

Important: Any recursive solution can be rewritten using loops. However, recursion can make some solutions clearer and more understandable.

When to use recursion:

The problem naturally divides into smaller, identical subproblems
The recursive solution is more intuitive than the iterative one
You're working with tree-like data structures
When to use loops:

Simple sequential processing
When performance is critical (loops are generally faster)
When the iterative solution is just as clear
Note: Python programmers often prefer iterative solutions for simple problems. For finding an item in a list, you'd typically use:

# More Pythonic approaches
index = names.index("Diana")  # Built-in method
found = "Diana" in names       # Membership test
Recursion truly shines with complex data structures like trees and graphs!

5. Creating Recursive Functions

5.1 The Two-Step Process

Creating a recursive function follows a simple pattern:

Step 1: Write the base case (when to stop recursing)
Step 2: Write the recursive case (how to break down the problem)

5.2 Example: Factorial
Step 1: Write the Base Case

"""

def factorial(n):
    """Calculate n! (n factorial)"""
    # Base case: 1! = 1 or 0! = 1
    if n <= 1:
        return 1

#Test just the base case:

print(factorial(1))  # Should print: 1
print(factorial(0))  # Should print: 1

"""
Step 2: Add the Recursive Case
"""
def factorial(n):
    """Calculate n! (n factorial)"""
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    else:
        return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(3))   # 6
print(factorial(10))  # 3628800

"""
5.3 Understanding the Execution

Let's trace factorial(4):


factorial(4)
    ├─ 4 * factorial(3)
    │      ├─ 3 * factorial(2)
    │      │      ├─ 2 * factorial(1)
    │      │      │      └─ returns 1 (base case)
    │      │      └─ returns 2 * 1 = 2
    │      └─ returns 3 * 2 = 6
    └─ returns 4 * 6 = 24
5.4 Important Note About Factorial

While factorial has a natural recursive definition, a loop is actually simpler for this problem:
"""

def factorial_iterative(n):
    """Iterative version - simpler for factorial"""
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

print(factorial_iterative(5))  # 120
"""
5.5 When to Use Recursion
Why show factorial then? It's an excellent teaching example because:

The mathematical definition is recursive
It's simple enough to understand easily
It demonstrates the recursive pattern clearly
When is recursion better? For problems like:

Tree traversal
Graph algorithms
Binary search
Divide-and-conquer algorithms
Data structures of unknown depth

6. Debugging Recursive Functions
Recursive functions can be challenging to debug because:

Multiple function calls are "stacked" on top of each other
It's hard to visualize what's happening at each level
Tracking values across different namespaces is confusing

Debugging Technique: Indented Print Statements

A powerful debugging trick is to add print statements that indent based on recursion depth:
"""


def find_debug(names, target, low, high, indent=""):
    """Binary search with debug output"""
    # Print what we're searching
    print(f"{indent}Searching for '{target}' in range [{low}, {high}]")
    
    mid = (low + high) // 2
    print(f"{indent}Middle index: {mid}, value: '{names[mid]}'")
    
    # Base case 1: Found
    if names[mid] == target:
        print(f"{indent}✓ Found '{target}' at index {mid}!")
        return mid
    
    # Base case 2: Not found
    if low == high:
        print(f"{indent}✗ Not found (search space exhausted)")
        return -1
    
    # Recursive cases
    if target < names[mid]:
        print(f"{indent}→ Searching lower half...")
        return find_debug(names, target, low, mid - 1, indent + "   ")
    else:
        print(f"{indent}→ Searching upper half...")
        return find_debug(names, target, mid + 1, high, indent + "   ")

# Test it
attendees = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
find_debug(attendees, "Frank", 0, len(attendees) - 1)
"""
Output:
Searching for 'Frank' in range [0, 6]
Middle index: 3, value: 'Diana'
→ Searching upper half...
   Searching for 'Frank' in range [4, 6]
   Middle index: 5, value: 'Frank'
   ✓ Found 'Frank' at index 5!

How the Indentation Works
Notice the indent parameter:

Initial call: indent = ""
First recursive call: indent = " " (3 spaces)
Second recursive call: indent = " " (6 spaces)
And so on...
This clearly shows the recursion depth visually!

Keeping Debug Code
Many programmers keep these debug statements in the code and comment them out when not needed:

"""

def find(names, target, low, high, indent=""):
    """Binary search with optional debugging"""
    # print(f"{indent}Searching for '{target}' in range [{low}, {high}]")
    
    mid = (low + high) // 2
    # print(f"{indent}Middle index: {mid}, value: '{names[mid]}'")
    
    if names[mid] == target:
        # print(f"{indent}✓ Found!")
        return mid
    
    if low == high:
        return -1
    
    if target < names[mid]:
        return find(names, target, low, mid - 1, indent + "   ")
    else:
        return find(names, target, mid + 1, high, indent + "   ")
"""

Mathematical Applications

7.1 The Fibonacci Sequence

The Fibonacci sequence is a famous mathematical sequence where each number is the sum of the two preceding ones:

Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

7.2 Recursive Fibonacci Implementation
"""

def fibonacci(n):
    """Return the nth Fibonacci number"""
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

"""
Output:
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34

7.4 Greatest Common Divisor (GCD)

The GCD is the largest number that divides evenly into two numbers.

Example: GCD(12, 8) = 4 (because 4 is the largest number that divides both 12 and 8)

Euclid's Algorithm (circa 300 BC)

The algorithm repeatedly subtracts the smaller number from the larger until they're equal:

GCD(12, 8)
= GCD(12 - 8, 8)
= GCD(4, 8)
= GCD(4, 8 - 4)
= GCD(4, 4)
= 4 ✓
7.5 Recursive GCD Implementation
"""

def gcd(a, b):
    """
    Calculate greatest common divisor using Euclid's algorithm
    """
    # Base case: numbers are equal
    if a == b:
        return a
    
    # Recursive case 1: a is larger
    if a > b:
        return gcd(a - b, b)
    
    # Recursive case 2: b is larger
    else:
        return gcd(a, b - a)

# Test it
print(f"GCD(12, 8) = {gcd(12, 8)}")     # 4
print(f"GCD(48, 18) = {gcd(48, 18)}")   # 6
print(f"GCD(100, 35) = {gcd(100, 35)}") # 5
"""
Output:
7.6 Tracing GCD Execution

Let's trace gcd(12, 8):


gcd(12, 8)
    ├─ 12 > 8, so call gcd(12-8, 8)
    │
    └─ gcd(4, 8)
           ├─ 8 > 4, so call gcd(4, 8-4)
           │
           └─ gcd(4, 4)
                  └─ 4 == 4, return 4 ✓
7.7 More Efficient GCD (Using Modulo)

The subtraction method works, but we can make it faster using the modulo operator:

"""

def gcd_efficient(a, b):
    """GCD using modulo (much faster)"""
    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return gcd_efficient(b, a % b)

print(f"GCD(48, 18) = {gcd_efficient(48, 18)}")  # 6

"""
Recursion Depth and Limits

8.1 What is Recursion Depth?

Recursion depth is the number of recursive function calls that have been made but haven't yet returned.

Think of it as how many functions are "stacked up" waiting to complete.

8.2 Why There's a Limit

Each recursive call uses memory to store:

Local variables
Parameters
Return address
If recursion goes too deep, you could run out of memory and crash the system!

8.3 Python's Recursion Limit

Python has a built-in safety limit to prevent infinite recursion:
"""

import sys

# Check the current limit
limit = sys.getrecursionlimit()
print(f"Current recursion limit: {limit}")  # Usually 1000
"""
8.4 What Happens When You Exceed the Limit?
"""
def infinite_recursion(n):
    """This will exceed the recursion limit!"""
    print(f"Call {n}")
    return infinite_recursion(n + 1)  # Never reaches base case!

# DON'T RUN THIS without being prepared!
# infinite_recursion(0)
# RecursionError: maximum recursion depth exceeded

#Example: Reaching the Limit

def count_calls(n):
    """Count how deep we can go"""
    if n <= 0:
        return 0
    return 1 + count_calls(n - 1)

try:
    result = count_calls(1000)
    print(f"Successfully made {result} calls")
except RecursionError as e:
    print(f"Hit recursion limit!")
    print(f"Error: {e}")


try:
    result = count_calls(2000)
    print(f"Successfully made {result} calls")
except RecursionError as e:
    print(f"Hit recursion limit!")
"""    
Output:
Hit recursion limit!
8.6 Changing the Recursion Limit

You can change the limit, but be careful!
"""

import sys

# Increase limit (use with caution!)
sys.setrecursionlimit(2000)

print(f"New limit: {sys.getrecursionlimit()}")  # 2000

# Now we can go deeper
result = count_calls(1500)
print(f"Successfully made {result} calls")
 Warning: Setting the limit too high can crash your program or even your system if you accidentally create infinite recursion!
"""
8.7 Better Solution: Use Iteration

For problems that require deep recursion, consider using iteration instead:
"""

# Recursive version (can hit limit)
def sum_to_n_recursive(n):
    if n <= 0:
        return 0
    return n + sum_to_n_recursive(n - 1)

# Iterative version (no limit issues)
def sum_to_n_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# This works fine
print(sum_to_n_iterative(10000))  # 50005000

# This would exceed recursion limit
# print(sum_to_n_recursive(10000))  # RecursionError!
"""
9. Best Practices and Common Pitfalls

9.1 Before Writing a Recursive Function

Ask yourself two key questions:

Question 1: Does this problem have a naturally recursive solution?

Examples of naturally recursive problems:

Binary search (divide range in half)
Tree traversal (visit node, then visit children)
Factorial
File system navigation (folder contains files and folders)

Examples of NOT naturally recursive:
Simple counting
Basic arithmetic operations
Linear array processing

Question 2: Is the recursive solution better than a non-recursive one?

Recursion is better when:
It makes the code significantly clearer
The problem is inherently recursive (like trees)
The depth won't exceed the recursion limit
Iteration is better when:

The loop version is just as clear
Performance is critical
Recursion depth could be very large
9.2 Example Comparison

Problem: Calculate 
This has no natural recursive solution. Just use direct computation:
"""

def energy(mass, speed_of_light):
    return mass * speed_of_light * speed_of_light
"""
Problem: Factorial (
n
!
n!)

Has a recursive definition, but a loop is simpler:
"""

# Recursive (demonstrates the concept)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative (better in practice)
def factorial_iterative(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

# 9.3 Common Errors to Avoid

#Error 1: Missing Base Case
# ❌ WRONG: No base case!
def countdown(n):
    print(n)
    countdown(n - 1)  # This will never stop!

# This will crash with RecursionError

# ✅ CORRECT: Has base case
def countdown(n):
    if n <= 0:  # Base case
        return
    print(n)
    countdown(n - 1)

# Error 2: Base Case Never Reached
# ❌ WRONG: Base case exists but is never reached
def factorial_wrong(n):
    if n == 1:  # What if n = 0? Or n is negative?
        return 1
    return n * factorial_wrong(n - 1)

# factorial_wrong(0) will crash!

# ✅ CORRECT: Handles all cases
def factorial_correct(n):
    if n <= 1:  # Covers n = 0 and n = 1
        return 1
    return n * factorial_correct(n - 1)

#Error 3: Infinite Recursion
# ❌ WRONG: Logic error prevents reaching base case
def broken_gcd(a, b):
    if a == b:
        return a
    if a > b:
        return broken_gcd(a + b, b)  # BUG: Should subtract, not add!
    else:
        return broken_gcd(a, b + a)

# This will never reach a == b!

# ✅ CORRECT: Moves toward base case
def correct_gcd(a, b):
    if a == b:
        return a
    if a > b:
        return correct_gcd(a - b, b)  # Subtract
    else:
        return correct_gcd(a, b - a)