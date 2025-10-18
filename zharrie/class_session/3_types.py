"""
A string is a sequence of characters that represents textual data like a person's name, a location, or a message to the user. 
A string can be created in various ways, such as from user input or from being defined in a program's source code. 
A string literal is a string defined in the source code of a program by surrounding the text value with single or double quotes, like 'MARY' or "MARY".
A string's characters are ordered from the string's first letter to the last. A character's position in a string is called that character's index. The first character is at index 0, the second at index 1, and so on. Ex: The string "Trish" has character "T" at index 0, character "r" at index 1, etc.
"""

# Get user's words
# relative = input("Enter a type of relative: ")

# food = input("Enter a type of food: ")

# adjective = input("Enter an adjective: ")

# period = input("Enter a time period: ")
# print()

# # Tell the story
# print("My", relative, "says eating", food)
# print("will make me more", adjective)
# print("so now I eat them every", period)
# print(type(relative))

"""
String indexing

Programs commonly access an individual character of a string. 
As a sequence type, every character in a string has an index starting at 0 from the leftmost character. 
For example, the "A" in string "ABC" is at index 0, "B" is at index 1, and "C" is at index 2. 
A programmer can reference a character at a specific index by appending brackets [ ] containing the desired index after the name of a string variable:

Note that negative indices can be used to reference characters starting from the right-most character of the string, instead of the left-most. Ex: alphabet[-1] is "Z".
"""
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(alphabet[0])   # Output: A
# print(alphabet[1])   # Output: B
# print(alphabet[25])  # Output: Z
# print(alphabet[-1])  # Output: Z
# print(alphabet[-2])  # Output: Y
# print(alphabet[-26]) # Output: A

# x = alphabet[-26]

# """
# Changing string variables

# Strings are immutable objects and a string variable cannot change once created. 
# Ex: name[2] = "B" is an invalid way to update a character in the name variable, and causes a TypeError when executed. 
# Instead, an assignment statement must be used to create a new string object to replace the old string.
# """

# name = "Mary"
# updated_name= name[:2] + "B" + name[3:]
# print(updated_name)  # Output: MaBy
# print(name)  # Output: Mary
# name = "Marty"
# print(name)  # Output: Marty
# # name[2] = "B"  # This would cause a TypeError
# print(name)  # Output: Marty
# print()
# # Get user's name
# name = input("Enter your name: ")
# print("Hello", name)
# print("Your name has", len(name), "letters in it.")
# print("The first letter of your name is", name[0])
# print("The last letter of your name is", name[-1])
# print("The middle letter of your name is", name[len(name)//2])


# """
# Formatted string literals (f-strings)

# Program output often includes expressions, such as variables or other calculations, as part of the output text. 
# A formatted string literal, or f-string, allows a programmer to create a string with placeholder expressions that are evaluated as the program executes. 
# An f-string starts with an f character before the starting quote and uses curly braces { } to denote the placeholder expressions. A placeholder expression is also called a replacement field, as its value replaces the expression in the final output.
# """
# name = input("Enter your name: ")
# print(f"Hello {name}")
# print(f"Your name has {len(name)} letters in it.")
# print(f"The first letter of your name is {name[0]}")
# print(f"The last letter of your name is {name[-1]}")
# print(f"The middle letter of your name is {name[len(name)//2]}")

# """
# An = sign is provided after the expression in a replacement field to print both the expression and its result, which is a useful debugging technique when dynamically generating lots of strings and output. Ex: f"{2*4=}" produces the string "2*4=8".

# Additionally, double braces {{ and }} are used to place a curly brace into an f-string. Ex: f"{{Jeff Bezos}}: Amazon" produces the string "{Jeff Bezos}: Amazon".
# """
# print(f"{2*4=}")  # Output: 2*4=8
# print(f"{{Jeff Bezos}}: Amazon")  # Output: {Jeff Bezos}: Amazon
# pi = 3.14159
# print(f"{pi:.2f}")  # Output: 3.14
# print(f"{pi:.4f}")  # Output: 3.1416
# print(f"{pi:.6f}")  # Output: 3.141590

# Lists Basics
"""
Creating a list

A container is a construct used to group related values together and contains references to other objects instead of data. 
A list is a container created by surrounding a sequence of variables or literals with brackets [ ]. Ex: my_list = [10, "abc"] creates a new list variable my_list that contains the two items: 10 and "abc". 
A list item is called an element. A list is mutable, meaning that the elements in a list can be replaced, reordered, or removed.

A list is also a sequence type, meaning the contained elements are ordered by position in the list, known as the element's index, starting with 0. my_list = [ ] creates an empty list with no elements.
"""
# my_list = [10, "abc"]
# empty_list = []
# print(my_list)      # Output: [10, 'abc']
# print(empty_list)   # Output: []
# print(my_list[0])   # Output: 10
# print(my_list[1])   # Output: abc
# print(my_list[-1])  # Output: abc
# print(my_list[-2])  # Output: 10
# print(len(my_list)) # Output: 2
# print(len(empty_list)) # Output: 0

# """
# Accessing list elements

# Lists are useful for reducing the number of variables in a program. 
# Instead of having a separate variable for the name of every student in a class, or for every word in an email, a single list can store an entire collection of related variables.

# Individual list elements can be accessed using an indexing expression by using brackets as in my_list[i], where i is an integer. 
# This allows a programmer to quickly find the i'th element in a list.

# A list's index must be an integer. 
# The index cannot be a floating-point type, even if the value is a whole number like 0.0 or 1.0. 
# Using any type besides an integer will produce a runtime error, and the program will terminate.
# """

# students = ["Alice", "Bob", "Charlie"]
# print(students[:2])  # Output: Alice
# print(students[1])  # Output: Bob
# print(students[2])  # Output: Charlie
# print(students[-1]) # Output: Charlie
# print(students[-2]) # Output: Bob
# print(students[-3]) # Output: Alice
# # print(students[3])  # This would cause an IndexError
# # print(students[-4]) # This would cause an IndexError  
# # print(students[1.0]) # This would cause a TypeError
# # print(students["1"]) # This would cause a TypeError
# print(len(students)) # Output: 3

# """
# Updating list elements

# Lists are mutable, meaning that a programmer can change a list's contents. 
# An element can be updated with a new value by performing an assignment to a position in the list.
# A list's length can be changed by adding or removing elements.
# # """
# students = ["Alice", "Bob", "Charlie"]
# print(students)  # Output: ['Alice', 'Bob', 'Charlie']
# students[1] = "Betty"
# print(students)  # Output: ['Alice', 'Betty', 'Charlie']
# students.append("David")
# print(students)  # Output: ['Alice', 'Betty', 'Charlie', 'David']
# students.remove("Alice")
# print(students)  # Output: ['Betty', 'Charlie', 'David']
# students.pop()
# print(students)  # Output: ['Betty', 'Charlie']
# students.insert(1, "Bob")
# print(students)  # Output: ['Betty', 'Bob', 'Charlie']
# students.sort()
# print(students)  # Output: ['Betty', 'Bob', 'Charlie']
# students.reverse()
# print(students)  # Output: ['Charlie', 'Bob', 'Betty']
# print(len(students)) # Output: 3

"""
Common list methods
A method is a function that is associated with an object.
A list has several useful methods that can be called to perform common operations on the list.
"""
# my_list = [3, 1, 4, 1, 5]
# print(my_list)          # Output: [3, 1, 4, 1, 5]
# print(len(my_list))     # Output: 5
# my_list.append(9)       # Add 9 to the end of the list
# print(my_list)          # Output: [3, 1, 4, 1, 5, 9]
# print(len(my_list))     # Output: 6
# my_list.remove(1)       # Remove the first occurrence of 1
# print(my_list)          # Output: [3, 4, 1, 5, 9]
# print(len(my_list))     # Output: 5
# my_list.pop()           # Remove and return the last element
# print(my_list)          # Output: [3, 4, 1, 5]
# print(len(my_list))     # Output: 4
# my_list.insert(1, 2)    # Insert 2 at index 1
# print(my_list)          # Output: [3, 2, 4, 1, 5]
# print(len(my_list))     # Output: 5
# my_list.sort()          # Sort the list in ascending order
# print(my_list)          # Output: [1, 2, 3, 4, 5]
# print(len(my_list))     # Output: 5
# my_list.reverse()       # Reverse the order of the list
# print(my_list)          # Output: [4, 3, 2, 1, 5]
# print(len(my_list))     # Output: 5
# my_list=[4, 3, 2,2, 1, 5]
# print("Counting in a list:",my_list.count(2)) # Output: 1
# print(my_list.index(3)) # Output: 1
# my_list.clear()         # Remove all elements from the list
# print(my_list)          # Output: []
# print(len(my_list))     # Output: 0

# """
# Sequence-type methods and functions

# Methods like append(), pop(), and remove() are sequence-type methods. Sequence-type methods are functions built into the Python language definitions of sequence types like lists and strings. All sequence-type objects have associated methods that typically alter or return some information about the object.

# Sequence-type functions are functions built into the Python language that take sequences like lists or strings as arguments and operate on the given sequences. They do not require an object or "." dot notation.Ex: len(my_list) retrieves the length of a sequence.
# Common sequence-type functions include:
# len(seq) - Returns the number of elements in the sequence seq.
# list1 + list2 - Returns a new list that is the concatenation of list1 and list2.
# list * n - Returns a new list that is the original list repeated n times.
# min(seq) - Returns the smallest element in the sequence seq.
# max(seq) - Returns the largest element in the sequence seq.
# sum(seq) - Returns the sum of all elements in the sequence seq (only for numeric sequences).
# sorted(seq) - Returns a new list containing all elements from the sequence seq in ascending order.
# reversed(seq) - Returns an iterator that accesses the elements of the sequence seq in reverse order.
# list.index(val) - Returns the index of the first occurrence of val in the list.
# list.count(val) - Returns the number of occurrences of val in the list.
# """
# numbers = [3, 1, 4, 1, 5]  
# print(len(numbers))        # Output: 5
# print(numbers + [9, 2, 6]) # Output: [3, 1, 4, 1, 5, 9, 2, 6]
# print(numbers * 2)        # Output: [3, 1, 4, 1, 5, 3, 1, 4, 1, 5]
# print(min(numbers))       # Output: 1
# print(max(numbers))       # Output: 5
# print(sum(numbers))       # Output: 14
# print(sorted(numbers))    # Output: [1, 1, 3, 4, 5]
# print(list(reversed(numbers))) # Output: [5, 1, 4, 1, 3]
# print(numbers.index(4))   # Output: 2
# print(numbers.count(1))   # Output: 2   

"""
Tuples

A tuple, usually pronounced "tuhple" or "toople," stores a collection of data, like a list, but is immutable – once created, the tuple's elements cannot be changed. A tuple is also a sequence type, supporting len(), indexing, and other sequence functions. A new tuple is generated by creating a list of comma-separated values, such as 5, 15, 20. Typically, tuples are surrounded with parentheses, as in (5, 15, 20). Note that printing a tuple always displays surrounding parentheses.

A tuple is not as common as a list in practical usage but can be useful when a programmer wants to ensure that values do not change. Tuples are typically used when element position, and not just the relative ordering of elements, is important. Ex: A tuple might store the latitude and longitude of a landmark because a programmer knows that the first element should be the latitude, the second element should be the longitude, and the landmark will never move from those coordinates.
"""
# my_tuple = (10, "abc", 3.14)
# empty_tuple = ()
# print(my_tuple)        # Output: (10, 'abc', 3.14)
# print(empty_tuple)     # Output: ()
# print(my_tuple[0])     # Output: 10
# print(my_tuple[1])     # Output: abc
# print(my_tuple[2])     # Output: 3.14
# print(my_tuple[-1])    # Output: 3.14
# print(my_tuple[-2])    # Output: abc
# print(my_tuple[-3])    # Output: 10
# print(len(my_tuple))   # Output: 3
# print(len(empty_tuple)) # Output: 0
# my_tuple[1] = "def"  # This would cause a TypeError
# print(my_tuple)      # This would not execute due to the error    

# """
# Named tuples

# A program commonly captures collections of data. Ex: a car is described using a series of variables describing the make, model, retail price, horsepower, and number of seats. A named tuple allows the programmer to define a new simple data type that consists of named attributes. A Car named tuple with fields like Car.price and Car.horsepower would more clearly represent a car object than a list with index positions correlating to some attributes.

# The namedtuple container must be imported to create a new named tuple. Once the container is imported, the named tuple should be created like in the example below, where the name and attribute names of the named tuple are provided as arguments to the namedtuple constructor. Note that the fields to include in the named tuple are found in a list, but the fields may also be a single string with space- or comma-separated values.
# """
# from collections import namedtuple
# Car = namedtuple("Car", ["make", "model", "price", "horsepower", "seats"])
# my_car = Car("Toyota", "Camry", 24000, 203, 5)
# print(my_car)               # Output: Car(make='Toyota', model='Camry', price=24000, horsepower=203, seats=5)
# print(my_car.make)        # Output: Toyota
# print(my_car.model)         # Output: Camry
# print(my_car.price)         # Output: 24000
# print(my_car.horsepower)    # Output: 203
# print(my_car.seats)         # Output: 5
# print(len(my_car))          # Output: 5
# my_car.price = 25000      # This would cause an AttributeError
# print(my_car)             # This would not execute due to the error   

# """
# namedtuple() creates only the new simple data type and does not create new data objects. 
# Above, a new data object is not created until Car() is called with appropriate values. 
# A data object's attributes can be accessed using dot notation, as in chevy_blazer.price. 
# This "named" attribute is simpler to read than a list or tuple referenced via index such as chevy_blazer[2].

# Like normal tuples, named tuples are immutable. 
# A programmer wishing to edit a named tuple would replace the named tuple with a new object.
# """

"""
Set basics

A set is an unordered collection of unique elements. A set has the following properties:
Elements are unordered: Elements in the set do not have a position or index.
Elements are unique: No elements in the set share the same value.
A set can be created using the set() function, which accepts a sequence-type iterable object (list, tuple, string, etc.) whose elements are inserted into the set. 
A set literal can be written using curly braces { } with commas separating set elements. Note that an empty set can only be created using set().
Because the elements of a set are unordered and have no meaningful position in the collection, the index operator is not valid. Attempting to access the element of a set by position, for example nums1[2] to access the element at index 2, is invalid and will produce a runtime error.

A set is often used to reduce a list of items that potentially contains duplicates into a collection of unique values. 
Simply passing a list into set() will cause any duplicates to be omitted in the created set.

Modifying sets

Sets are mutable elements can be added or removed using set methods. 
The add() method places a new element into the set if the set does not contain an element with the provided value. The remove() and pop() methods remove an element from the set.

Additionally, sets support the len() function to return the number of elements in a set. To check if a specific value exists in a set, a membership test such as value in set (discussed in another section) can be used.
Adding elements to a set:

set.add(value): Add value into the set. Ex: my_set.add("abc")
Remove elements from a set:

set.remove(value): Remove the element with given value from the set. Raises KeyError if value is not found. Ex: my_set.remove("abc")
set.pop(): Remove a random element from the set. Ex: my_set.pop()
set.discard(value): Remove the element with given value from the set if it exists. Does nothing if value is not found. Ex: my_set.discard("abc")
set.clear(): Remove all elements from the set. Ex: my_set.clear()
"""

# my_set = {1, 2, 3, 4, 5,5}
# empty_set = set()
# print(my_set)        # Output: {1, 2, 3, 4, 5}
# print(empty_set)     # Output: set()
# print(len(my_set))   # Output: 5
# # print(my_set[0])    # This would cause a TypeError
# # print(my_set[-1])   # This would cause a TypeError
# # print(my_set[1.0])  # This would cause a TypeError
# # print(my_set["1"])  # This would cause a TypeError    
# print(len(my_set))   # Output: 5    
# my_set.add(6)        # Add 6 to the set
# print(my_set)        # Output: {1, 2, 3, 4, 5, 6}
# print(len(my_set))   # Output: 6
# my_set.add(3)        # Adding 3 again has no effect
# print(my_set)        # Output: {1, 2, 3, 4, 5, 6}
# print(len(my_set))   # Output: 6
# set1.update(set2) = {7, 8}  # Add multiple elements from another set
# print(my_set)        # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# print(len(my_set))   # Output: 8
# my_set.remove(2)     # Remove 2 from the set
# print(my_set)        # Output: {1, 3, 4, 5, 6}
# print(len(my_set))   # Output: 5
# my_set.discard(7)    # Discarding 7 has no effect
# print(my_set)        # Output: {1, 3, 4, 5, 6}
# print(len(my_set))   # Output: 5
# my_set.pop()         # Remove and return an arbitrary element
# print(my_set)        # Output: {3, 4, 5, 6} (actual output may vary)
# print(len(my_set))   # Output: 4 (actual output may vary)
# my_set.clear()       # Remove all elements from the set
# print(my_set)        # Output: set()
# print(len(my_set))   # Output: 0    

"""
Set operations

Python set objects support typical set theory operations such as intersections and unions. Provided below is a brief overview of common set operations supported in Python:
set.intersection(set_a, set_b, set_c...) - Returns a new set containing elements common to all provided sets. Ex: set1.intersection(set2)
set.union(set_a, set_b, set_c...) - Returns a new set containing all unique elements from all provided sets. Ex: set1.union(set2)
set.difference(set_a, set_b) - Returns a new set containing elements in set_a that are not in set_b. Ex: set1.difference(set2)
set.symmetric_difference(set_a, set_b) - Returns a new set containing elements in either set_a or set_b but not in both. Ex: set1.symmetric_difference(set2)
set.issubset(set_a) - Returns True if the set is a subset of set_a, otherwise returns False. Ex: set1.issubset(set2)
set.issuperset(set_a) - Returns True if the set is a superset of set_a, otherwise returns False. Ex: set1.issuperset(set2)  
set.isdisjoint(set_a) - Returns True if the set has no elements in common with set_a, otherwise returns False. Ex: set1.isdisjoint(set2)
"""
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1)                     # Output: {1, 2, 3, 4, 5}
# print(set2)                     # Output: {4, 5, 6, 7, 8}
# print(set1.intersection(set2))  # Output: {4, 5}
# print(set1.union(set2))         # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# print(set1.difference(set2))    # Output: {1, 2, 3}
# print(set2.difference(set1))    # Output: {6, 7, 8}
# print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}
# print(set1.issubset({1, 2, 3, 4, 5, 6})) # Output: True
# print(set1.issuperset({1, 2, 3})) # Output: True
# print(set1.isdisjoint({6, 7, 8})) # Output: True
# print(set1.isdisjoint({3, 4, 5})) # Output: False   

"""
Creating a dictionary

Consider a normal English language dictionary. 
A reader looks up the word "cat" and finds the definition, "A small, domesticated carnivore." 
The relationship between "cat" and its definition is associative, i.e., "cat" is associated with words describing "cat."

A dictionary is a Python container used to describe associative relationships. 
A dictionary is represented by the dict object type. A dictionary associates (or "maps") keys with values. 
A key is a term that can be located in a dictionary, such as the word "cat" in the English dictionary. 
A value describes some data associated with a key, such as a definition. 
A key can be any immutable type, such as a number, string, or tuple; a value can be any type.

A dict object is created using curly braces { } to surround the key:value pairs that comprise the dictionary contents. 
Ex: players = {"Lionel Messi": 10, "Cristiano Ronaldo": 7} creates a dictionary called players with two keys: "Lionel Messi" and "Cristiano Ronaldo", associated with the values 10 and 7 (their respective jersey numbers). 
An empty dictionary is created with the expression players = { }.

Dictionaries are typically used in place of lists when an associative relationship exists. 
Ex: If a program contains a collection of anonymous student test scores, those scores should be stored in a list. 
However, if each score is associated with a student name, a dictionary could be used to associate student names to their score. 
Other examples of associative relationships include last names and addresses, car models and price, or student ID number and university email address.

Though dictionaries maintain a left-to-right ordering, dictionary entries cannot be accessed by indexing. To access an entry, the key is specified in brackets [ ]. If no entry with a matching key exists in the dictionary, then a KeyError runtime error occurs and the program is terminated.
Dictionaries are mutable, meaning that entries can be added, removed, or changed.

Adding, modifying, and removing dictionary entries

A dictionary is mutable, so entries can be added, modified, and deleted as necessary by a programmer. A new dictionary entry is added by using brackets to specify the key: prices["banana"] = 1.49. A dictionary key is unique; attempting to create a new entry with a key that already exists in the dictionary replaces the existing entry. The del keyword is used to remove entries from a dictionary: del prices["papaya"] removes the entry whose key is "papaya". If the requested key to delete does not exist, then a KeyError occurs.

Adding new entries to a dictionary:

dict[k] = v: Adds the new key-value pair k-v, if dict[k] does not already exist.
Example: students["John"] = "A+"
Modifying existing entries in a dictionary:

dict[k] = v: Updates the existing entry dict[k], if dict[k] already exists.
Example: students["Jessica"] = "A+"
Removing entries from a dictionary:

del dict[k]: Deletes the entry dict[k].
Example: del students["Rachel"]
"""
# players = {"Lionel Messi": 10, "Cristiano Ronaldo": 7}
# empty_dict = {}
# print(players)        # Output: {'Lionel Messi': 10, 'Cristiano Ronaldo': 7}
# print(empty_dict)     # Output: {}  
# print(len(players))   # Output: 2
# print(len(empty_dict)) # Output: 0      
# print(players["Lionel Messi"])      # Output: 10
# print(players["Cristiano Ronaldo"])  # Output: 7
# # print(players["Neymar"])           # This would cause a KeyError  
# print("Lionel Messi" in players)      # Output: True
# print("Neymar" in players)            # Output: False
# print("Neymar" not in players)        # Output: True
# print("Cristiano Ronaldo" not in players) # Output: False
# players["Neymar"] = 11
# print(players)        # Output: {'Lionel Messi': 10, 'Cristiano Ronaldo': 7, 'Neymar': 11}
# print(len(players))   # Output: 3
# players["Cristiano Ronaldo"] = 9
# print(players)        # Output: {'Lionel Messi': 10, 'Cristiano Ronaldo': 9, 'Neymar': 11}
# print(len(players))   # Output: 3
# del players["Neymar"]
# print(players)        # Output: {'Lionel Messi': 10, 'Cristiano Ronaldo': 9}
# print(len(players))   # Output: 2
# players.clear()
# print(players)        # Output: {}
# print(len(players))   # Output: 0   

# """
# Common data types

# Numeric types int and float represent the most common types used to store data. All numeric types support the normal mathematical operations such as addition, subtraction, multiplication, and division, among others.
# Common numeric data types.
# Type	Notes
# int	Numeric type: Used for variable-width integers.
# float	Numeric type: Used for floating-point numbers.

# Sequence types string, list, and tuple are containers for collections of objects ordered by position in the sequence, where the first object has an index of 0 and subsequent elements have indices 1, 2, etc. 
# A list and a tuple are very similar, except that a list is mutable and individual elements may be edited or removed. Conversely, a tuple is immutable and individual elements may not be edited or removed. 
# Lists and tuples can contain any type, whereas a string contains only single characters. 
# A programmer can apply sequence-type functions such as len() and element indexing using brackets [ ] to any sequence type.

# The only mapping type in Python is the dict type. Like a sequence type, a dict serves as a container. 
# However, each element of a dict is independent, having no special ordering or relation to other elements. 
# A dictionary uses key-value pairs to associate a key with a value.
# Sequence types string, list, and tuple are containers for collections of objects ordered by position in the sequence, where the first object has an index of 0 and subsequent elements have indices 1, 2, etc. A list and a tuple are very similar, except that a list is mutable and individual elements may be edited or removed. Conversely, a tuple is immutable and individual elements may not be edited or removed. Lists and tuples can contain any type, whereas a string contains only single characters. A programmer can apply sequence-type functions such as len() and element indexing using brackets [ ] to any sequence type.

# The only mapping type in Python is the dict type. Like a sequence type, a dict serves as a container. However, each element of a dict is independent, having no special ordering or relation to other elements. A dictionary uses key-value pairs to associate a key with a value.

# Type	Notes
# string	Sequence type: Used for text.
# list	Sequence type: A mutable container with ordered elements.
# tuple	Sequence type: An immutable container with ordered elements.
# set	Set type: A mutable container with unordered and unique elements.
# dict	Mapping type: A container with key-values associated elements.


# Choosing a container type

# New programmers often struggle with choosing a container type that best fits their needs, such as a list, tuple, or dict. 
# In general, a programmer might use a list when data has an order, such as lines of text on a page. 
# A programmer might use a tuple instead of a list if the contained data should not change. 
# If order is not important, a programmer might use a dictionary to capture relationships between elements, such as student names and grades.
# # """

# """
# Type conversions

# A calculation sometimes must mix integer and floating-point numbers. For example, given that about 50.4% of human births are males, then 0.504 * num_births calculates the number of expected males in num_births. If num_births is an integer type, then the expression combines a floating point and integer.

# A type conversion is a conversion of one type to another, such as an integer to a float. An implicit conversion is a type conversion automatically made by the interpreter, usually between numeric types. For example, the result of an arithmetic operation like + or * will be a float only if either operand of the operation is a float.

# 1 + 2 returns an integer type.
# 1 + 2.0 returns a float type.
# 1.0 + 2.0 returns a float type.
# integer-to-float conversion is straightforward: 25 becomes 25.0.

# float-to-integer conversion just drops the fraction: 4.9 becomes 4.
# A programmer can explicitly convert a value from one type to another using a type conversion function.
# int(x) - Converts x to an integer type.
# float(x) - Converts x to a floating-point type.
# str(x) - Converts x to a string type.
# list(iterable) - Converts an iterable (like a string or tuple) to a list.
# tuple(iterable) - Converts an iterable (like a string or list) to a tuple.
# set(iterable) - Converts an iterable (like a string, list, or tuple) to a set.
# dict(mapping) - Converts a mapping (like a list of key-value pairs) to a dictionary.
# """
# print(int(4.9))      # Output: 4
# print(int(-4.9))     # Output: -4
# print(float(4))      # Output: 4.0
# print(float(-4))     # Output: -4.0
# print(str(123))      # Output: '123'
# print(str(3.14))     # Output: '3.14'
# print(list("abc"))   # Output: ['a', 'b', 'c']
# print(tuple("abc"))  # Output: ('a', 'b', 'c')
# print(set("aabbcc")) # Output: {'a', 'b', 'c'}
# print(dict([("a", 1), ("b", 2)])) # Output: {'a': 1, 'b': 2}
# print(dict((("x", 10), ("y", 20)))) # Output: {'x': 10, 'y': 20}
# print(dict(a=1, b=2)) # Output: {'a': 1, 'b': 2}        

# """
# Binary numbers

# Normally, a programmer thinks in terms of base 10 numbers. However, a computer must allocate some finite quantity of bits (e.g., 32 bits) for a variable, and that quantity of bits limits the range of numbers that the variable can represent. Python allocates additional memory to accommodate numbers of large sizes (past a typical 32 or 64 bit size), and a Python programmer need not think of such low-level details. However, binary base computation is an important part of computer science, so some background on how the quantity of bits influences a variable's number range is helpful.

# Because each memory location is composed of bits (0s and 1s), a processor stores a number using base 2, known as a binary number.

# For a number in the more familiar base 10, known as a decimal number, each digit must be 0-9, and each digit's place is weighed by increasing powers of 10.
# In base 2, each digit must be 0-1 and each digit's place is weighted by increasing powers of 2.

# """
print(0b101)   # Output: 5 (binary 101 is decimal 5)
print(0b111)   # Output: 7 (binary 111 is decimal 7)
print(0b1001)  # Output: 9 (binary 1001 is decimal 9)
print(0b1111)  # Output: 15 (binary 1111 is decimal 15)
print(0b10000) # Output: 16 (binary 10000 is decimal 16)
print(0b11111) # Output: 31 (binary 11111 is decimal 31)
print(0b100000) # Output: 32 (binary 100000 is decimal 32)
print(0b111111) # Output: 63 (binary 111111 is decimal 63)
print(0b1000000) # Output: 64 (binary 1000000 is decimal 64)
print(0b1111111) # Output: 127 (binary 1111111 is decimal 127)
print(0b10000000) # Output: 128 (binary 10000000 is decimal 128)
print(0b11111111) # Output: 255 (binary 11111111 is decimal 255)
print(0b100000000) # Output: 256 (binary 100000000 is decimal 256)







