#Functions
"""
A program may perform the same operation repeatedly, causing a large and confusing program due to redundancy. Program redundancy can be reduced by creating a grouping of predefined statements for repeated operations, known as a function. 
Even without redundancy, functions can prevent a main program from becoming large and confusing.

Function basics

A function is a named series of statements.

A function definition consists of the function's name and a block of statements. Ex: def calc_pizza_area(): is followed by an indented block of statements.
A function call is an invocation of the function's name, causing the function's statements to execute.
Python comes with a number of built-in functions, such as input(), int(), len(), etc. The def keyword is used to create new functions.
A function may optionally accept arguments, which are values passed into the function to customize its operation.
A function may optionally return a value to the code that called it, using the return statement.
Good practice is to follow the convention of naming functions with lowercase letters and underscores, such as get_name or calc_area.

Return statements

A function may return one value using a return statement. Below, the compute_square() function returns the square of its argument.
A function can return only one item, not two or more (though a list or a tuple with multiple elements could be returned). A function with no return statement, or a return statement with no following expression, returns the value None. None is a special keyword that indicates no value.

A return statement may appear at any point in a function, not just as the last statement. A function may also contain multiple return statements in different locations.
"""
# design a function without parameters
def say_hello():
    return "Hello, World!"
print(say_hello())  # Outputs: Hello, World!    

def add_numbers(a, b):
    return a + b
print(add_numbers(3, 5))  # Outputs: 8
print(add_numbers(-2, 7))  # Outputs: 5 

def compute_square(x):
    return x * x
result = compute_square(5)
print(result)  # Outputs: 25    

#Example of a function with multiple return statements
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(10))  # Outputs: Positive
print(check_number(-5))  # Outputs: Negative
print(check_number(0))   # Outputs: Zero    

"""
Parameters

A programmer can influence a function's behavior via an input.

A parameter is a function input specified in a function definition. Ex: A pizza area function might have diameter as an input.
An argument is a value provided to a function's parameter during a function call. 
Ex: A pizza area function might be called as calc_pizza_area(12.0) or as calc_pizza_area(16.0).

A parameter is like a variable definition. 
Upon entering the function, the parameter is bound to the argument object provided by the call, creating a shared reference to the object. 
Upon return, the parameter can no longer be used.

An argument may be an expression, like 12.0, x, or  x * 1.5.

A function definition with no parameters must still have the parentheses, as in: def calc_something():. 
The call to such a function must include parentheses and must be empty, as in: calc_something().

"""
def calc_pizza_area(diameter):
    radius = diameter / 2
    area = 3.14159 * radius * radius
    return area
print(calc_pizza_area(12.0))  # Outputs: 113.09724
print(calc_pizza_area(16.0))  # Outputs: 201.06176  

#Example of multiple parameters
def greet_user(first_name, last_name):  
    return f"Hello, {first_name} {last_name}!"
print(greet_user("John", "Doe"))  # Outputs: Hello, John Doe!
print(greet_user("Jane", "Smith"))  # Outputs: Hello, Jane Smith!


"""
Hierarchical function calls

A function's statements may include function calls, known as hierarchical function calls or nested function calls. 
Code such as user_input = int(input()) consists of such a hierarchical function call, in which the input() function is called and evaluates to a value that is then passed as an argument to the int() function.
"""
def calc_circle_area(circle_diameter):
2	    pi_val = 3.14159265
3	   
4	    circle_radius = circle_diameter / 2.0
5	    circle_area = pi_val * circle_radius * circle_radius
6	    return circle_area
7	
8	def calc_pizza_calories(pizza_diameter):
9	    calories_per_square_inch = 16.7    # Regular crust pepperoni pizza
10	   
11	    total_calories = calc_circle_area(pizza_diameter) * calories_per_square_inch
12	    return total_calories
13	
14	
15	print(f"12 inch pizza has {calc_pizza_calories(12.0):.2f} calories.")
16	print(f"14 inch pizza has {calc_pizza_calories(14.0):.2f} calories.")

"""
Printing from a function

A common operation for a function is to print text. Large text outputs can clutter the main program, especially if the text needs to be output multiple times. 
A function that only prints typically does not return a value. 
A function with no return statement is called a void function, and such a function returns the value None.

"""
def print_welcome_message():
    print("Welcome to the program!")
    print("This program demonstrates functions.")
    print("Enjoy using it!")    
print_welcome_message()  # Call the function to print the message
result = print_welcome_message()  # Call the function and capture its return value
print(result)  # Outputs: None, since the function does not return a value

"""
Dynamic and static typing

A programmer can pass any type of object as an argument to a function. 
Consider a function add(x, y) that adds the two parameters:

A programmer can call the add() function using two integer arguments, as in add(5, 7), which returns a value of 12. 
Alternatively, a programmer can pass in two string arguments, as in add("Tora", "Bora"), which would concatenate the two strings and return "ToraBora".

The function's behavior of adding together different types is a concept called polymorphism. Polymorphism is an inherent part of the Python language. For example, consider the multiplication operator *. If the two operands are numbers, then the result is the product of those two numbers. If one operand is a string and the other an integer (e.g., "x" * 5), then the result is a repetition of the string five times: "xxxxx".

Python uses dynamic typing to determine the type of objects as a program executes. Ex: The consecutive statements num = 5 and num = "7" first assign with an integer type and then a string type. The type of num can change depending on the value it references. The interpreter is responsible for checking that all operations are valid as the program executes. If the function call add(5, "100") is evaluated, an error is generated when adding the string to an integer.

In contrast to dynamic typing, many other languages like C, C++, and Java use static typing, which requires the programmer to define the type of every variable and every function parameter in a program's source code. Ex: string name = "John" declares a string variable in C++. When the source code is compiled, the compiler attempts to detect non type-safe operations, and halts the compilation process if such an operation is found.

Dynamic typing typically allows for more flexibility of the code that a programmer can write, but at the expense of potentially introducing more bugs, since there is no compilation process by which types can be checked.
"""

def add(x, y):
    return x + y    
print(add(5, 7))            # Outputs: 12 (integer addition)
print(add("Tora", "Bora"))  # Outputs: ToraBora (string concatenation)
# print(add(5, "100"))      # Uncommenting this line would raise a TypeError    

# Reasons for defining functions
"""
Improving program readability

Programs can become hard for humans to read and understand. Decomposing a program into functions can aid program readability, yield an initially correct program, and ease future maintenance. 
The following program contains two user-defined functions, making the main program (after the function definitions) easier to read and understand. For larger programs, the effect is even greater.
"""
"""
Modular program development

Programmers commonly use functions to write programs modularly. Modular development is the process of dividing a program into separate modules that can be developed and tested separately and integrated into a single program.

A programmer can use function stubs (described in depth elsewhere) to capture the high-level behavior of the required functions (or modules) before diving into the details of each function, like planning a route for a road trip before starting to drive.
"""
"""
Avoid writing redundant code

A function can be defined once, then called from multiple places in a program, thus avoiding redundant code. Examples of such functions are math module functions like sqrt() that relieve a programmer from having to write several lines of code each time a square root needs to be computed.

The skill of decomposing a program's behavior into a good set of functions is a fundamental part of programming that helps characterize a good programmer. Each function should have easily recognizable behavior, and the behavior of the main program (and any function that calls other functions) should be easily understandable via the sequence of function calls.

A general guideline (especially for beginner programmers) is that a function's definition usually shouldn't have more than about 30 lines of code, although this guideline is not a strict rule.
"""

# Mathematical functions
"""
A function is defined as a mathematical calculation involving several numerical parameters and returning a numerical result.
"""
def calc_rectangle_area(length, width):
    return length * width   
def calc_triangle_area(base, height):
    return 0.5 * base * height
def calc_circle_area(radius):
    pi = 3.14159
    return pi * radius * radius
"""
Calling functions in expressions

A function call evaluates to its returned value. 
Thus, a function call often appears within an expression. Ex: 5 + compute_square(4) would become 5 + 16, or 21. 
A function that returns None cannot be used as such within an expression.
"""
total_area = calc_rectangle_area(5, 10) + calc_circle_area(7) + calc_triangle_area(6, 8)
print(f"Total area: {total_area:.2f}")  # Outputs the total area with 2 decimal places  

"""
Modular functions for mathematical expressions

Modularity allows more complex functions to incorporate simpler functions. 
Complex mathematical functions often call other mathematical functions. 
Ex: A function that calculates the volume or surface area of a cylinder calls a function that returns the area of the cylinder's base, which is needed for both calculations.
"""
import math

def calc_circular_base_area(radius):
   return math.pi * radius * radius

def calc_cylinder_volume(baseRadius, height):
   return calc_circular_base_area(baseRadius) * height

def calc_cylinder_surface_area(baseRadius, height):
   return (2 * math.pi * baseRadius * height) + (2 * calc_circular_base_area(baseRadius))

radius = float(input("Enter base radius: "))
height = float(input("Enter height: "))

print(f"Cylinder volume: {calc_cylinder_volume(radius, height):.3f}")
print(f"Cylinder surface area: {calc_cylinder_surface_area(radius, height):.3f}")

# Function stubs
"""
To assist with the incremental development process, programmers commonly introduce function stubs, which are function definitions whose statements haven't been written yet. The benefit of a function stub is that the high-level behavior of the program can be captured before diving into details of each function, akin to planning the route of a road trip before starting to drive. Capturing high-level behavior first may lead to better-organized code, reduced development time, and code with fewer bugs.

A programmer writing a function stub should consider whether or not calling the unwritten function is a valid operation. Simply doing nothing and returning nothing may be acceptable early in the development of a larger program. One approach is to use the pass keyword, which performs no operation except to act as a placeholder for a required statement.
"""     
def placeholder_function():
    pass  # Placeholder for future implementation
# Example of a function stub with a return value
def compute_area(length, width):
    return 0  # Placeholder return value
# Example of a function stub that raises an error
def not_implemented_function():
    raise NotImplementedError("This function is not yet implemented.")  

"""
Another useful approach is to print a message when a function stub is called, thus alerting the user to the missing function statements. 
Good practice is for a stub to return -1 for a function that will have a return value. 
"""

# Functions with branches/loops
"""
A function's block of statements may include branches, loops, and other statements.
"""
# Example of a function with a loop to find the maximum value in a list
def find_maximum(numbers):
    if not numbers:
        return None  # Handle empty list
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
print(find_maximum([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Outputs: 9
print(find_maximum([]))  # Outputs: None   

# Functions are objects
"""
A function is also an object in Python, having a type, identity, and value. A function definition like def print_face(): creates a new function object with the name print_face bound to that object.

A part of the value of a function object is compiled bytecode that represents the statements to be executed by the function. A bytecode is a low-level operation, such as adding, subtracting, or loading from memory. One Python statement might require multiple bytecode operations.
"""
def print_face():
    print("  ^   ^  ")
    print("    -    ")
    print(" \\_____/ ")
print(type(print_face))  # Outputs: <class 'function'>
print(id(print_face))    # Outputs: (some integer representing the function's identity)
print(print_face)        # Outputs: <function print_face at 0x...> (some memory address)
print(print_face())      # Outputs the face and then None, since the function does not return a value

# Functions: Common errors
"""
Copy-paste errors

A common error is to copy and paste code among functions but not complete all necessary modifications to the pasted code.
For example, a programmer might copy and paste code from one function to another but forget to change the function name in a return statement, causing the function to call itself recursively instead of calling the intended function.
"""
# Example of a copy-paste error
def calculate_area(length, width):
    return length * width   
def calculate_perimeter(length, width):
    return 2 * (length + width)  # Corrected from calculate_area to calculate_perimeter 
"""
Return errors

Another common error is to return the wrong variable.
For example, a programmer might intend to return the variable area but mistakenly return the variable radius, which may not even be defined in the function.
"""
# Example of a return error
def calculate_area(length, width):
    area = length * width
    return area  # Corrected from returning radius to returning area


"""
Another common error is to fail to return a value for a function. If execution reaches the end of a function's statements without encountering a return statement, then the function returns a value of None. If the function is expected to return an actual value, then such an assignment can cause confusion.
"""
# Example of a missing return statement
def calculate_area(length, width):
    area = length * width
    # Missing return statement!

# Scope of variables and functions
"""
Variable and function scope

A variable or function object is only visible to part of a program, known as the object's scope. When a variable is created inside a function, the variable's scope is limited to inside that function. In fact, because a variable's name does not exist until bound to an object, the variable's scope is actually limited to after the first assignment of the variable until the end of the function.
A variable created inside a function is known as a local variable, and the function is known as the variable's defining function. A local variable is not visible outside its defining function. 
"""
def my_function():
    local_var = 42  # local_var is a local variable
    print(local_var)  # This works fine
my_function()
# print(local_var)  # This would raise a NameError, as local_var is not defined outside the function

"""
Global variables

In contrast, a variable defined outside of a function is called a global variable. A global variable's scope extends from the assignment to the end of the file and can be accessed inside of functions.
A function can read a global variable, but if the function assigns to a variable with the same name as a global variable, then the function creates a new local variable that shadows the global variable.
A global statement must be used to change the value of a global variable inside of a function. Ex: global_var = 100 creates a global variable. The function below can read the value of global_var, but if it assigns to global_var without a global statement, then a new local variable named global_var is created that shadows the global variable.

Assignment of global variables in functions should be used sparingly. If a local variable (including a parameter) has the same name as a global variable, then the naming can be confusing to a reader. Furthermore, if a function updates the global variable, then that function's behavior is no longer limited to its parameters and return value; the function may have side effects that are hard for a programmer to recognize. Good practice is to limit the use of global variables to defining constants that are independent of any function. Global variables should be avoided (with a few exceptions), especially by beginner programmers.

A function also has scope, which extends from the function's definition to the end of the file. To call a function, the interpreter must have evaluated the function definition (thus binding the function name to a function object). An attempt to call a function before a function has been defined results in an error.
"""
global_var = 100  # global variable
def my_function():
    print(global_var)  # This works fine, accessing the global variable
    local_var = 42     # This is a local variable
    print(local_var)   # This works fine, accessing the local variable
my_function()
print(global_var)  # This works fine, accessing the global variable

# print(local_var)  # This would raise a NameError, as local_var is not defined outside the function    
def modify_global():
    global global_var  # Declare that we want to use the global variable
    global_var = 200   # Modify the global variable
modify_global()
print(global_var)  # Outputs: 200, showing that the global variable was modified    

# Namespaces and scope resolution
"""
A namespace maps names to objects. The Python interpreter uses namespaces to track all of the objects in a program. 
For example, when executing z = x + y, the interpreter looks in a namespace to find the value of the objects referenced by x and y, evaluates the expression, and then updates z in the namespace with the expression's result.
A namespace is a normal Python dictionary whose keys are the names and whose values are the objects. A programmer can examine the names in the current local and global namespace by using the  locals() and globals() built-in functions.
A program has several namespaces, including a global namespace and a local namespace for each function. The global namespace contains all of the global variables and functions defined in the program. 
Each function has its own local namespace that contains the function's parameters and local variables. When a function is called, a new local namespace is created for that call, which is destroyed when the function returns.
"""

"""
Scope and scope resolution

Scope is the area of code where a name is visible. Namespaces are used to make scope work. Each scope, such as global scope or a local function scope, has its own namespace. If a namespace contains a name at a specific location in the code, then that name is visible and a programmer can use it in an expression.

At least three nested scopes are active at any point in a program's execution:

Built-in scope – Contains all of the built-in names of Python, such as int(), str(), list(), range(), etc.
Global scope – Contains all globally defined names outside of any functions.
Local scope – Refers to scope within the currently executing function but is the same as global scope if no function is executing.
When looking up a name, the interpreter first searches the local namespace, then the global namespace, and finally the built-in namespace (which contains names like print and int). This search order is known as the LEGB rule: Local, Enclosing, Global, Built-in.
"""

def outer_function():
    outer_var = "outer"
    def inner_function():
        inner_var = "inner"
        print(inner_var)   # Looks in local namespace of inner_function
        print(outer_var)   # Looks in enclosing namespace of outer_function
        print(global_var)  # Looks in global namespace
    inner_function()
outer_function()
print(global_var)  # Looks in global namespace 
# print(outer_var)  # This would raise a NameError, as outer_var is not defined in the global namespace
# print(inner_var)  # This would raise a NameError, as inner_var is not defined in the global namespace 

# Function arguments
"""
Function arguments and mutability

Arguments to functions are passed by object reference, a concept known in Python as pass-by-assignment. 
When a function is called, new local variables are created in the function's local namespace by binding the names in the parameter list to the passed arguments.
The semantics of passing object references as arguments is important because modifying an argument that is referenced elsewhere in the program may cause side effects outside of the function scope. When a function modifies a parameter, whether or not that modification is seen outside the scope of the function depends on the mutability of the argument object.

If the object is immutable, such as a string or integer, then the modification is limited to inside the function. Any modification to an immutable object results in the creation of a new object in the function's local scope, thus leaving the original argument object unchanged.
If the object is mutable, then in-place modification of the object is seen outside the scope of the function. Any operation like adding elements to a container or sorting a list that is performed within a function will also affect any other variables in the program that reference the same object.
"""
def modify(num_list):
2	    num_list[1] = 99
3	
4	my_list = [10, 20, 30]
5	modify(my_list)
6	print(my_list)  # my_list still contains 99!

"""
Sometimes a programmer needs to pass a mutable object to a function but wants to make sure that the function does not modify the object at all. One method to avoid unwanted changes is to pass a copy of the object as the argument instead, like in the statement my_func(num_list[:]).
"""

def modify(num_list):
    num_list[1] = 99  # Modifying only the copy
	
my_list = [10, 20, 30]
modify(my_list[:])  # Pass a copy of the list. The [:] syntax creates a slice of the entire list, which results in a new copy

print(my_list)  # my_list does not contain 99!

# Keyword arguments and default parameter values
"""
Keyword arguments

Sometimes a function requires many arguments. In such cases, a function call can become very long and difficult to read. 
Furthermore, a programmer might easily make a mistake when calling such a function if the ordering of the arguments is given incorrectly.
"""
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description("The Lord of the Rings", "J. R. R. Tolkien", "George Allen & Unwin", 
                       1954, 1.0, 22, 456)
# The above call is hard to read and error-prone
# Using keyword arguments for clarity
print_book_description(title="The Lord of the Rings", author="J. R. R. Tolkien", 
                       publisher="George Allen & Unwin", year=1954, version=1.0, 
                       num_chapters=22, num_pages=456)
# The above call is clearer and less error-prone
"""
Python provides for keyword arguments that allow arguments to map to parameters by name, instead of implicitly by position in the argument list. 
When using keyword arguments, the argument list does not need to follow a specific order.
Keyword arguments can be mixed with positional arguments, provided that the keyword arguments come last. 
A common error is to place keyword arguments before all position arguments, which generates an exception.
"""

"""
Default parameter values

Sometimes a function has parameters that are optional. A function can have a default parameter value for one or more parameters, meaning that a function call can optionally omit an argument, and the default parameter value will be substituted for the corresponding omitted argument.

The following function prints a date in a particular style, given parameters for day, month, and year. The fourth parameter indicates the desired style, with 0 meaning American style, and 1 meaning European style. For July 30, 2012, the American style is 7/30/2012 and the European style is 30/7/2012.
"""
def print_date(day, month, year, style=0):
    if style == 0:
        print(f"{month}/{day}/{year}")  # American style
    else:
        print(f"{day}/{month}/{year}")  # European style
print_date(30, 7, 2012)        # Uses default style (American)
print_date(30, 7, 2012, 1)     # Uses European style
print_date(30, 7, 2012, style=1)  # Uses European style with keyword argument

"""
If a parameter does not have a default value, then failing to provide an argument (either keyword or positional) generates an error.

A common error is to provide a mutable object, like a list, as a default parameter. Such a definition can be problematic because the default argument object is created only once, at the time the function is defined (when the script is loaded), and not every time the function is called. Modification of the default parameter object will persist across function calls, which is likely not what a programmer intended. The below program demonstrates the problem with mutable default objects and illustrates a solution that creates a new empty list each time the function is called.
"""
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []  # Create a new list if none was provided
    my_list.append(value)
    return my_list
print(append_to_list(1))  # Outputs: [1]
print(append_to_list(2))  # Outputs: [2], not [1, 2]
print(append_to_list(3, [10, 20]))  # Outputs: [10, 20, 3]
print(append_to_list(4))  # Outputs: [4], not [1, 2, 4] 

"""
Mixing keyword arguments and default parameter values

Mixing keyword arguments and default parameter values allows a programmer to omit arbitrary arguments from a function call. Because keyword arguments use names instead of position to match arguments to parameters, any argument can be omitted as long as that argument has a default value.

Consider the print_date function from above. If every parameter has a default value, then the user can use keyword arguments to pass specific arguments anywhere in the argument list. 
"""
def print_date(day=1, month=1, year=2000, style=0):
    # ...


print_date(day=30, year=2012)   # Defaults:        month=1,            style=0
print_date(style=1)             # Defaults: day=1, month=1, year=2000
print_date(year=2012, month=4)  # Defaults: day=1,        style=0

"""
Arbitrary arguments

Sometimes a programmer doesn't know how many arguments a function requires. A function definition can include an *args parameter that collects optional positional parameters into an arbitrary argument list tuple.
Adding a final function parameter of **kwargs, short for keyword arguments, creates a dictionary containing "extra" arguments not defined in the function definition. The keys of the dictionary are the parameter names specified in the function call.
The * and ** characters in *args and **kwargs are the important symbols. Using "args" and "kwargs" is standard practice, but any valid identifier is acceptable (like perhaps using *condiments in the sandwich example).

One or both of *args or **kwargs can be used. They must come last (and in that order if both are used) in the parameter list, otherwise an error occurs.
"""
def print_all_args(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)    
print_all_args(1, 2, 3, name="Alice", age=30)
# Outputs:
# Positional arguments (args): (1, 2, 3)
# Keyword arguments (kwargs): {'name': 'Alice', 'age': 30}  
print_all_args("hello", 42)
# Outputs:
# Positional arguments (args): ('hello', 42)
# Keyword arguments (kwargs): {}
print_all_args()
# Outputs:
# Positional arguments (args): ()
# Keyword arguments (kwargs): {}

"""
Multiple function outputs

Occasionally a function should produce multiple output values. However, function return statements are limited to returning only one value. A workaround is to package the multiple outputs into a single container, commonly a tuple, and return that container.
"""
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return total, count, average  # Returns a tuple with three values
stats = calculate_stats([10, 20, 30, 40, 50])
print(f"Total: {stats[0]}, Count: {stats[1]}, Average: {stats[2]}")  

"""
Unpacking is an operation that allows a statement to perform multiple assignments at once to variables in a tuple or list.
"""
total, count, average = calculate_stats([10, 20, 30, 40, 50])
print(f"Total: {total}, Count: {count}, Average: {average}")    


"""
Help! Using docstrings to document functions
Docstrings

A large program can contain many functions with a wide variety of uses. A programmer should document each function, giving a high-level description of the purpose of the function, so that later readers of the code can easily understand. A docstring is a string literal placed in the first line of a function body.

A docstring starts and ends with three consecutive quotation marks. Good practice is to keep the docstring of a simple function as a single line, including the quotes. Furthermore, there should be no blank lines before or after the docstring.

Multi-line docstrings can be used for more complicated functions to describe the function arguments. Multi-line docstrings should use consistent indentation for each line, separating the ending triple-quotes by a blank line.
"""

"""
The help() function

The help() function can aid a programmer by providing them with all the documentation associated with an object. A statement such as help(ticket_price) would print out the docstring for the ticket_price() function, providing the programmer with information about how to call that function.
The help() function works with most of the built-in Python names, since the language creators provided docstrings for many items. Notice that the output of help depends on the object passed as an argument. If the argument is a function, then the docstring is printed. If you have studied classes or modules, note how help(str) prints out a description of the string str class methods, and how help(math) prints out all the contents of the math module.
"""
def ticket_price(age):
    """Calculate the ticket price based on age.
    
    Parameters:
    age (int): The age of the person.
    
    Returns:
    float: The ticket price.
    """
    if age < 5:
        return 0.0
    elif age < 18:
        return 10.0
    elif age < 65:
        return 20.0
    else:
        return 15.0 
print(ticket_price(30))  # Outputs: 20.0
print(ticket_price(70))  # Outputs: 15.0
help(ticket_price)  # Displays the docstring for the ticket_price function