# Lists
"""
The list type is one of Python’s most important and widely used data structures.
- A container groups related objects.
- A list is a mutable container, meaning its size can change and its elements can be modified in place.
- Lists are also sequences, so elements have a left-to-right order and can be accessed by index.
- Each element in a list may be of any type—strings, numbers, other lists, etc.
"""
# Creating Lists
# Use square brackets:
my_list = [1, "cat", 3.14]
#Or use the list() constructor with an iterable:
list("abc")  # → ["a", "b", "c"]

#Indexing
"""
Indices are zero-based. my_list[4] accesses the 5th element.
The index can be any integer expression:
"""
i = 2
my_list[i]  # accesses the 3rd element
"""
Example: oldest_people[nth_person - 1] retrieves the nth person’s age.
Indices must be integers, not floats (my_list[1.0] is invalid).

Common Operations
Lists support many of the same operations as strings:
- Accessing elements
- Slicing (my_list[1:3])
- Concatenation (list1 + list2)
Slicing and concatenation return new lists.

Mutability and In-Place Modification
Unlike strings, lists can be modified directly:
- Adding/removing elements
- Updating existing elements
Because lists are mutable, multiple variables can reference the same list object. Changing the list through one variable affects the other:
my_teams = ["Celtics", "Bulls"]
your_teams = my_teams
my_teams[1] = "Lakers"
print(your_teams)  # → ["Celtics", "Lakers"]

To avoid unintentional side effects, make a copy:
your_teams = my_teams[:]  # creates a new list
"""

# List Methods
"""
Python provides many built-in list methods for adding, removing, modifying, and querying elements. Most of these methods modify the list in place, meaning the underlying list object is changed — and any variable referencing that list will see the change.

Adding Elements
Method	            Description	                            Example	                                Result
list.append(x)	    Adds x to the end of the list.	        my_list=[5,8]; my_list.append(16)	    [5, 8, 16]
list.extend([x])	Adds all items from another iterable.	my_list=[5,8]; my_list.extend([4,12])	[5, 8, 4, 12]
list.insert(i, x)	Inserts x before index i.	            my_list=[5,8]; my_list.insert(1,1.7)	[5, 1.7, 8]

Removing Elements
Method	            Description	                            Example	                                Result
list.remove(x)	    Removes the first occurrence of x.	    my_list=[5,8,14]; my_list.remove(8)	    [5, 14]
list.pop()	        Removes & returns the last item.	    my_list=[5,8,14]; val=my_list.pop()	    [5,8], val=14
list.pop(i)	        Removes & returns item at index i.	    my_list=[5,8,14]; val=my_list.pop(0)	[8,14], val=5

Modifying Elements
Method	            Description	                            Example	                                Result
list.sort()	        Sorts items in ascending order.	        my_list=[14,5,8]; my_list.sort()	    [5, 8, 14]
list.reverse()	    Reverses the order of items.	        my_list=[14,5,8]; my_list.reverse()	    [8, 5, 14]

Miscellaneous
Method	            Description	                            Example	                                Result
list.index(x)	    Returns index of first occurrence of x.	my_list=[5,8,14]; my_list.index(14)	    2
list.count(x)	    Counts occurrences of x.	            my_list=[5,8,5,5,14]; my_list.count(5)	3

Best Practices
Prefer list methods for clarity instead of alternatives like del my_list[0] or my_list[len(my_list):] = [val].
sort() and reverse() rearrange elements in place.
index() and count() only retrieve information and do not modify the list.
"""
# Example Usage
# Creating a list of numbers
numbers = [10, 20, 30, 40, 50]  
# Accessing elements
first_number = numbers[0]  # 10
last_number = numbers[-1]   # 50
# Modifying elements
numbers[1] = 25  # Now numbers is [10, 25, 30, 40, 50]
# Adding elements
numbers.append(60)  # Now numbers is [10, 25, 30, 40, 50, 60]
# Removing elements
numbers.remove(30)  # Now numbers is [10, 25, 40, 50, 60]
# Sorting the list
numbers.sort()  # Now numbers is [10, 25, 40, 50, 60]
# Counting occurrences
count_25 = numbers.count(25)  # 1
# Finding index
index_50 = numbers.index(50)  # 3
print(numbers)  # Output: [10, 25, 40, 50, 60]

"""
Iterating over a list
Accessing each element of a list is a fundamental task in Python programming. Iteration is typically done with a for loop, which is designed for traversing sequences.
Each iteration of a for loop assigns the next element of the list to a loop variable (e.g., my_var), executes the loop body, and then continues with the following element until the sequence ends.

Example: Finding the Maximum Even Number

Suppose the user enters:
7, -9, 55, 44, 20, -400, 0, 2

A program might:
- Use a loop to convert the string input into integers and append them to a list.
- Use another loop to display the numbers.
- Iterate again to determine the largest even number.

To track the largest value, the program uses a variable (e.g., max_even). During each iteration, if the current element is even and greater than max_even, the variable is updated.
A common mistake is initializing max_even to 0. If the list only contains 0 or negative numbers, the result will be incorrect. Example:
nums = [-1, 0, -16, -2]
would mistakenly assign -2 as the max even.
To avoid this, the correct approach is initializing max_even = None and updating it properly within the loop.

For Loops with Iterables
A for loop works with any iterable object, not just lists. Strings, tuples, and many other objects in Python can be iterated over.

Index Errors and enumerate()
Accessing a list outside its valid index range (e.g., my_list[10] for an 8-element list) raises an IndexError and halts execution.
To safely combine indices with values during iteration, Python provides enumerate(). Example:
for pos, token in enumerate(nums):
    print(pos, token)
This loop assigns both the index (pos) and the value (token) on each iteration.

Built-in Functions for Iteration
Python offers built-in functions to perform common operations without writing explicit loops:

Function	Description	                                                Example	        Output
all(list)	True if all elements are truthy, or if the list is empty	all([1,2,3])	True
any(list)	True if at least one element is truthy	                    any([0,2])	    True
max(list)	Returns the largest element	                                max([-3,5,25])	25
min(list)	Returns the smallest element	                            min([-3,5,25])	-3
sum(list)	Returns the total of all elements	                        sum([-3,5,25])	27

These shortcuts eliminate the need for writing custom tracking logic with loops in many cases.
"""
# Example: Finding the Maximum Even Number
user_input = input("Enter numbers separated by commas: ")
num_strings = user_input.split(",")
numbers = []
for num_str in num_strings:
    numbers.append(int(num_str))    
print("You entered:", numbers)
max_even = None
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        if max_even is None or num > max_even:
            max_even = num
if max_even is not None:
    print("The largest even number is:", max_even)
else:
    print("No even numbers were entered.")  

# List nesting
"""
Because lists can store any type of object—and lists themselves are objects—a list can contain other lists as elements. This is called list nesting.

Example:
my_list = [[5, 13], [50, 75, 100]]
Here, my_list contains two elements, each of which is itself a list.
A standard list is one-dimensional, holding a linear sequence of values (e.g., times, temperatures, or data samples). Nesting makes it possible to represent multi-dimensional data structures, such as tables, grids, or game boards.

Iterating Through Nested Lists
To process all elements in a nested list, programmers typically use nested for loops:
The outer loop iterates over the elements of the outer list (e.g., rows of a table).
The inner loop iterates over the elements of each inner list (e.g., columns).

Example:
First outer iteration: row = [1, 5, 10]
Inner iterations: cell = 1, then 5, then 10
By combining nested loops with enumerate(), you can easily keep track of both row and column indices during iteration.
"""
# Example: Iterating Through a Nested List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]   
for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
        print(f"Element at ({row_index}, {col_index}): {value}")    

# List slicing
"""
Slice notation lets a programmer extract multiple elements from a list, producing a new list with only the specified items. A slice uses the form my_list[start:end], where:
- start is the index of the first element to include.
- end marks the stopping point but is not included in the result.

Example:
boston_bruins = ["Tyler", "Zdeno", "Patrice"]
print(boston_bruins[0:2])   # ['Tyler', 'Zdeno']
print(boston_bruins[1:3])   # ['Zdeno', 'Patrice']

To include the last element in a slice, specify an end index beyond the list’s length.

Negative Indices
Negative numbers count backward from the end of the list. For instance:
election_years = [2000, 2004, 2008, 2012]
print(election_years[0:-1])   # [2000, 2004, 2008]

This approach is particularly useful when the list length is unknown, as it avoids explicitly calculating len(my_list)-1.

Stride
A slice can also include a stride, written as my_list[start:end:stride]. The stride determines how many elements to skip between selections.

Example:
my_list = [5, 10, 20, 40, 80]
print(my_list[0:5:2])   # [5, 20, 80]

By default, the stride is 1, so my_list[0:5] and my_list[0:5:1] are equivalent.

Common List Slicing Patterns
Operation	                Description	                        Example	                        Output
my_list[start:end]	        Elements from start to end-1	    [5, 10, 20][0:2]	            [5, 10]
my_list[start:end:stride]	Every stride element in range	    [5, 10, 20, 40, 80][0:5:3]	    [5, 40]
my_list[start:]	            From start to end	                [5, 10, 20, 40, 80][2:]	        [20, 40, 80]
my_list[:end]	            From beginning to end-1	            [5, 10, 20, 40, 80][:4]	        [5, 10, 20, 40]
my_list[:]	                Full copy of list	                [5, 10, 20, 40, 80][:]	        [5, 10, 20, 40, 80]

Handling Edge Cases
Python evaluates out-of-range slice indices gracefully:
If end exceeds the list length, the slice stops at the end.
If end < start, the result is an empty list.
"""
# Example: List Slicing
data = [10, 20, 30, 40, 50, 60]
first_three = data[:3]  # [10, 20, 30]
last_two = data[-2:]    # [50, 60]
every_second = data[::2]  # [10, 30, 50]
reversed_data = data[::-1]  # [60, 50, 40, 30, 20, 10]
print("First three:", first_three)
print("Last two:", last_two)
print("Every second:", every_second)
print("Reversed:", reversed_data)   

# Loops modifying lists
"""
Programs sometimes need to loop through a list while updating its elements — either by changing values or adjusting the list’s size.
Updating Element Values
You can combine len() and range() to iterate by index and directly update list elements. For example:
my_list = [5, 10, 15]
for i in range(len(my_list)):
    my_list[i] += 5
print(my_list)  # → [10, 15, 20]
This approach increments each element by 5.

Changing List Size
A common mistake is adding or removing items from a list while iterating over it. Doing so can cause skipped elements, duplicated checks, or other unintended behavior.
To avoid this, work on a copy of the list during iteration. The simplest method is to use slice notation ([:]), which creates a shallow copy:
for item in my_list[:]:
    # Safe to add, remove, or modify elements here
This ensures that loop iterations are not disrupted by modifications to the original list.
"""
# Example: Modifying a List While Iterating
original_list = [1, 2, 3, 4, 5]
# Increment each element by 10
for i in range(len(original_list)):
    original_list[i] += 10
print("Incremented List:", original_list)  # [11, 12, 13, 14, 15]   
# Safely remove even numbers while iterating over a copy
for num in original_list[:]:
    if num % 2 == 0:
        original_list.remove(num)
print("After Removing Evens:", original_list)  # [11, 13, 15]   

# List Comprehensions
"""
When a programmer wants to apply the same operation to every element of a list, Python offers list comprehensions—a concise way to iterate, modify elements, and create a new list in a single expression.
Syntax:
new_list = [expression for item in iterable if condition]
- expression: Operation applied to each element.
- item: Variable representing each element in the iterable.
- iterable: Collection being looped over (list, string, tuple, etc.).
- condition (optional): Filter to include only elements that satisfy the condition.

A list comprehension has three main components:
- Expression – Evaluated for each element.
- Loop variable – Binds to each element during iteration.
- Iterable – The object being iterated over. 
The brackets indicate that the comprehension returns a new list. Conceptually, it is equivalent to a for loop that applies the expression to each element and collects the results.

Why Use List Comprehensions?
- More concise than equivalent for loops.
- Often more efficient due to internal optimizations by Python.
- Produces a new list, rather than modifying an existing one.

Examples: For Loops vs List Comprehensions
#	Task	For Loop	List Comprehension	Output
1	Add 10 to each element	my_list=[5,20,50]; for i in range(len(my_list)): my_list[i]+=10	my_list = [i+10 for i in my_list]	[15, 30, 60]
2	Convert each element to string	for i in range(len(my_list)): my_list[i]=str(my_list[i])	[str(i) for i in my_list]	['5','20','50']
3	Convert user input to integers	my_list=[]; for i in inp.split(): my_list.append(int(i))	[int(i) for i in inp.split()]	[7,9,3]
4	Sum of each row in 2D list	sum_list=[]; for row in my_list: sum_list.append(sum(row))	[sum(row) for row in my_list]	[30,21,100]
5	Minimum row sum in 2D list	sum_list=[]; for row in my_list: sum_list.append(sum(row)); min_row=min(sum_list)	min([sum(row) for row in my_list])	21

Notes:
List comprehensions always create a new list; for loops can modify an existing list.
The iterable component can be an expression, e.g., inp.split() in example 3.
Comprehensions can also be used inside functions, e.g., min([sum(row) for row in my_list]).

Conditional List Comprehensions
You can filter elements using an optional if clause:
new_list = [expression for item in iterable if condition]
Only elements satisfying the condition are included in the resulting list.
"""
# Example: List Comprehensions
# Using a for loop to create a list of squares
squares_loop = []
for i in range(10):
    squares_loop.append(i * i)
print("Squares using loop:", squares_loop)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]   
# Using a list comprehension to create a list of squares
squares_comp = [i * i for i in range(10)]
print("Squares using comprehension:", squares_comp)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]   
# Using a list comprehension with a condition to filter even squares
even_squares = [i * i for i in range(10) if i % 2 == 0]
print("Even squares:", even_squares)  # [0, 4, 16, 36, 64]  

# Sorting lists
"""
The sort() method is a powerful list operation that rearranges elements in place, ordering them from smallest to largest. Sorting follows standard comparison rules:
- Numbers are compared by value.
- Strings are compared using ASCII/Unicode codes.
- Lists are compared element by element.

For example, numeric elements like 5 and 10 are ordered based on their actual values.
my_list = [10, 5, 20]
my_list.sort()
print(my_list)  # [5, 10, 20]
Important: list.sort() modifies the original list, whereas the built-in sorted() function performs the same operation but returns a new sorted list without changing the original.

Using the key Argument
Both sort() and sorted() accept an optional key argument, which applies a function to each element before comparison. Common key functions include str.lower, str.upper, and str.capitalize.

Example:
names = ["Alice", "bob", "Charlie"]
sorted_names = sorted(names, key=str.lower)
print(sorted_names)  # ['Alice', 'bob', 'Charlie']
Without key=str.lower, lowercase names may appear at the end because "a" has a higher ASCII value than "A".
The key function can be any callable. For instance, sorting a two-dimensional list by the maximum value in each row can be done with key=max:
matrix = [[1, 5], [3, 2]]
sorted_matrix = sorted(matrix, key=max)

Using the reverse Argument
The reverse argument is a Boolean that flips the sort order:
sorted([15, 20, 25], reverse=True)  # [25, 20, 15]
reverse=False (default) → lowest to highest
reverse=True → highest to lowest

Combining key and reverse provides flexible sorting options, e.g., sorting strings alphabetically in reverse ignoring case:
sorted(names, key=str.lower, reverse=True)
"""
# Example: Sorting Lists
# Sorting a list of numbers
numbers = [42, 7, 19, 73, 3]
numbers.sort()
print("Sorted numbers:", numbers)  # [3, 7, 19, 42, 73]   
# Sorting a list of strings (case-sensitive)
fruits = ["banana", "Apple", "cherry", "date"]
fruits.sort()
print("Case-sensitive sorted fruits:", fruits)  # ['Apple', 'banana', 'cherry', 'date']   
# Sorting a list of strings (case-insensitive)
fruits_case_insensitive = ["banana", "Apple", "cherry", "date"]
fruits_case_insensitive.sort(key=str.lower)
print("Case-insensitive sorted fruits:", fruits_case_insensitive)  # ['Apple', 'banana', 'cherry', 'date']   
# Sorting a list of tuples by the second element
data = [(1, 'b'), (2, 'a'), (3, 'c')]
data.sort(key=lambda x: x[1])
print("Sorted by second element:", data)  # [(2, 'a'), (1, 'b'), (3, 'c')]   
# Sorting in reverse order
numbers_desc = [42, 7, 19, 73, 3]
numbers_desc.sort(reverse=True)
print("Numbers sorted in descending order:", numbers_desc)  # [73, 42, 19, 7, 3]

# Dictionaries
"""
A dictionary is a container type distinct from sequences like lists, tuples, or strings. Dictionaries store key-value pairs, where each key maps to a corresponding value—similar to how words in a traditional dictionary map to definitions. Starting with Python 3.7, dictionaries maintain the order in which items are inserted. The built-in dict type implements dictionaries in Python.

Creating Dictionaries
- Using braces {}: Wrap key-value pairs in curly braces. Keys and values can be literals or variables.
grades = {"Jose": "A+", "Gino": "C-"}
Here, "Jose" maps to "A+" and "Gino" maps to "C-".
Dictionary comprehension: Similar to list comprehensions, it evaluates a loop to create a new dictionary. (This is beyond the current scope.)

- Using the dict() function:
With keyword arguments:
dict(Bobby="805-555-2232", Johnny="951-555-0055")
With a list of tuples:
dict([("Bobby", "805-555-2232"), ("Johnny", "951-555-0055")])
Both methods produce equivalent dictionaries.

Common Dictionary Operations
Operation	                Description	                                    Example
my_dict[key]	            Accesses the value associated with a key	    jose_grade = my_dict["Jose"]
my_dict[key] = value	    Adds a new entry or updates an existing one	    my_dict["Jose"] = "B+"
del my_dict[key]	        Deletes a key-value pair	                    del my_dict["Jose"]
key in my_dict	            Checks if a key exists in the dictionary	    if "Jose" in my_dict: ...

Nested and Complex Values
Dictionaries can store values of any type, including other containers. For example:
my_dict["Jason"] = ["B+", "A-"]
This creates an entry for "Jason" whose value is a list of grades.
"""
# Example: Creating and Using a Dictionary
# Creating a dictionary using braces
student_grades = {"Alice": "A", "Bob": "B+", "Charlie": "A-"}
# Accessing a value
alice_grade = student_grades["Alice"]  # "A"
# Updating a value
student_grades["Bob"] = "A"
# Adding a new key-value pair
student_grades["David"] = "B"
# Deleting a key-value pair
del student_grades["Charlie"]
# Checking if a key exists
has_david = "David" in student_grades  # True
print(student_grades)  # Output: {'Alice': 'A', 'Bob': 'A', 'David': 'B'}       
# Creating a dictionary using the dict() function
contact_info = dict(John="  555-1234", Jane="555-5678")
# Accessing a value
john_phone = contact_info["John"]  # "555-1234"
# Updating a value
contact_info["John"] = "555-4321"
# Adding a new key-value pair
contact_info["Doe"] = "555-8765"
# Deleting a key-value pair
del contact_info["Jane"]
# Checking if a key exists
has_jane = "Jane" in contact_info  # False
print(contact_info)  # Output: {'John': '555-4321', 'Doe': '555-8765'}      

# Dictionary methods
"""
A dictionary method is a function provided by the dictionary type (dict) that operates on a specific dictionary object. Dictionary methods can perform useful operations, such as adding or removing elements, obtaining all the keys or values in the dictionary, merging dictionaries, etc.

Dictionary methods:

Dictionary method	        Description	                                 
my_dict.clear()	            Removes all items from the dictionary.	                                                                            
my_dict.get(key, default)	Reads the value of the key from the dictionary.
                            If the key does not exist in the dictionary, then  
                            returns default.print(my_dict.get("Jane", "N/A"))   
my_dict1.update(my_dict2)	Merges dictionary my_dict1 with another dictionary my_dict2. 
                            Existing entries in my_dict1 are overwritten if the same keys exist in my_dict2.
my_dict.pop(key, default)	Removes and returns the key value from the dictionary. If key does not exist, then default is returned.
Modification of dictionary elements using the above methods is performed in-place. Ex: Following the evaluation of the statement my_dict.pop("Ahmad"), any other variables that reference the same object as my_dict will also reflect the removal of "Ahmad". As with lists, a programmer should be careful not to modify dictionaries without realizing that other references to the objects may be affected.
"""
# Example: Using Dictionary Methods
# Creating a dictionary
employee_info = {"Alice": "Engineer", "Bob": "Manager", "Charlie": "Intern"}
# Using get() to access a value with a default
alice_role = employee_info.get("Alice", "N/A")  # "Engineer"
david_role = employee_info.get("David", "N/A")  # "N/A"
# Using update() to merge another dictionary
new_info = {"David": "Designer", "Eve": "Analyst"}
employee_info.update(new_info)
# Using pop() to remove and return a value
bob_role = employee_info.pop("Bob", "N/A")  # "Manager"
unknown_role = employee_info.pop("Frank", "N/A")  # "N/A"
# Using clear() to remove all items
employee_info.clear()
print(employee_info)  # Output: {}  # Output: {}    
print("Alice's role:", alice_role)  # Output: Engineer
print("David's role:", david_role)  # Output: N/A
print("Bob's role:", bob_role)  # Output: Manager
print("Unknown role:", unknown_role)  # Output: N/A 
print("Employee info after updates:", employee_info)  # Output: {}
# Example: Merging Two Dictionaries
dict1 = {"A": 1, "B": 2}
dict2 = {"B": 3, "C": 4}
dict1.update(dict2)
print("Merged Dictionary:", dict1)  # Output: {'A': 1, 'B': 3, 'C': 4}  
# Example: Using pop() with Default Value
my_dict = {"X": 10, "Y": 20}
value_x = my_dict.pop("X", "Not Found")  # 10
value_z = my_dict.pop("Z", "Not Found")  # "Not Found"
print("Value of X:", value_x)  # Output: Value of X: 10
print("Value of Z:", value_z)  # Output: Value of Z: Not Found
print("Dictionary after pops:", my_dict)  # Output: {'Y': 20}   

# Iterating over a dictionary
"""
As with other container types, a common task in programming is to iterate through a dictionary to access or modify its elements. A standard for loop can be used, where the loop variable takes on each key in the dictionary during iteration. Keys are traversed in the order they were inserted. Internally, Python generates a hash for each key—a unique value that enables fast lookups. While iteration order generally follows insertion, hash values may vary across Python versions and environments.
for key in my_dict:  
    # Code using my_dict[key]
# Code executed after the loop

Dictionary View Objects
The dict type provides the methods items(), keys(), and values(), each returning a view object. A view object allows read-only access to dictionary entries and reflects any updates to the dictionary. Programs can iterate over these views to access keys, values, or key-value pairs as needed.
dict.items() → yields (key, value) tuples
dict.keys() → yields keys
dict.values() → yields values
View objects are lazy, producing elements one at a time instead of generating a full list. This is memory-efficient but means indexing is not supported—attempting my_dict.keys()[0] will raise an error. To perform list operations, convert the view into a list using list(). For example, you can convert dictionary keys into a list and sort them:
planets_list = list(planets_dict.keys())
planets_list.sort()

Using dict.items() with Unpacking
The items() method is especially useful because it returns (key, value) tuples. These tuples can be unpacked directly in the loop, similar to enumerate(), giving both the key and value without additional lookups:
for key, value in my_dict.items():
    print(f"{key}: {value}")
This approach simplifies the code while iterating over dictionary entries.
"""
# Example: Iterating Over a Dictionary
# Creating a dictionary
fruit_prices = {"apple": 0.99, "banana": 0.59, "cherry": 2.99}
# Iterating over keys
for fruit in fruit_prices:
    print(f"{fruit}: ${fruit_prices[fruit]}")
# Iterating over items (key-value pairs)
for fruit, price in fruit_prices.items():
    print(f"{fruit}: ${price}")
# Iterating over keys using keys() method
for fruit in fruit_prices.keys():
    print(f"Fruit: {fruit}")
# Iterating over values using values() method
for price in fruit_prices.values():
    print(f"Price: ${price}")
# Converting keys to a list and sorting
sorted_fruits = list(fruit_prices.keys())
sorted_fruits.sort()
print("Sorted fruits:", sorted_fruits)  # Output: ['apple', 'banana', 'cherry']
# Example: Using dict.items() with Unpacking
for fruit, price in fruit_prices.items():
    print(f"The price of {fruit} is ${price}")  
# Output:
# The price of apple is $0.99
# The price of banana is $0.59
# The price of cherry is $2.99

# Dictionary nesting
"""
A dictionary can contain other dictionaries as values, forming a nested dictionary structure.
For example, the variable students can be initialized as an empty dictionary:
students = {}
A new entry is created using an indexing operation, where the key "Jose" maps to another dictionary. To access elements in the nested dictionary, use consecutive bracket [] operators:
students["Jose"]["Grade"]
The first set of brackets retrieves the nested dictionary associated with "Jose", and the second set indexes into that dictionary to access the value of "Grade".

Benefits and Structure
Nested dictionaries provide a simple but powerful data structure. A data structure organizes data logically and coherently, and nesting containers like dictionaries or lists offers greater flexibility for representing hierarchical or multi-level data.
Proper indentation and spacing improve readability and make the data hierarchy clear. These formatting choices do not affect the dictionary contents, as Python ignores whitespace in multi-line dictionary declarations.
Using nested dictionaries often makes code more readable and maintainable, particularly when keys represent meaningful categories, such as "Homeworks". In contrast, nested lists usually require additional loops and variables, which can complicate the code.
Dictionaries also support arbitrary levels of nesting. For instance, an expression like:
students["Jose"]["Homeworks"][2]["Grade"]
accesses a value in a dictionary nested four levels deep.
"""
# Example: Creating and Using a Nested Dictionary
# Creating a nested dictionary
students = {
    "Jose": {
        "Grade": "A",
        "Homeworks": [
            {"Title": "HW1", "Grade": 95},
            {"Title": "HW2", "Grade": 88},
            {"Title": "HW3", "Grade": 92}
        ]
    },
    "Gino": {
        "Grade": "B+",
        "Homeworks": [
            {"Title": "HW1", "Grade": 85},
            {"Title": "HW2", "Grade": 90},
            {"Title": "HW3", "Grade": 87}
        ]
    }
}
# Accessing a nested value
jose_grade = students["Jose"]["Grade"]  # "A"
gino_hw2_grade = students["Gino"]["Homeworks"][1]["Grade"]  # 90
# Updating a nested value
students["Jose"]["Homeworks"][0]["Grade"] = 97  # Update HW1
# Adding a new homework entry for Gino
students["Gino"]["Homeworks"].append({"Title": "HW4", "Grade": 93})
# Iterating over the nested dictionary
for student, info in students.items():
    print(f"{student}'s overall grade: {info['Grade']}")
    for hw in info["Homeworks"]:
        print(f"  {hw['Title']}: {hw['Grade']}")
# Output:
# Jose's overall grade: A
#   HW1: 97
#   HW2: 88
#   HW3: 92
# Gino's overall grade: B+
#   HW1: 85
#   HW2: 90
#   HW3: 87
#   HW4: 93 