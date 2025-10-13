# letter1 = "a"
# letter2 = "?"
# while letter1 <= "z":  # Outer loop
#     letter2 = "a"
#     while letter2 <= "z":  # Inner loop
#         print(f"{letter1}{letter2}.com")
#         letter2 = chr(ord(letter2) + 1)
#     letter1 = chr(ord(letter1) + 1)

#     # How many times does the inner loop execute?
# count = 0
# for i in range(4):
#    for j in range(3):
#       count = count + 1
# print(count)

# Developing programs incrementally
"""
As programs increase in complexity, a programmer's development process becomes more important. 
A programmer should not write the entire program and then run the program hoping the program works. 
If the program does not work on the first try, debugging can be extra difficult because the program may have many bugs.
"""

#Example: Phone number program
"""
The following program allows the user to enter a phone number that includes letters, which appear on phone keypads along with numbers, and are used by companies as a marketing tactic (e.g., 1-555-HOLIDAY). 
The program then outputs the phone number using numbers only.
# """
# # First version
# user_input = input("Enter phone number: ")

# index = 0
# for character in user_input:
#     print(f"Element {index} is: {character}")
#     index += 1

#     #incremental development.

#     user_input = input("Enter phone number: ")
# phone_number = ""

# for character in user_input:
#     if "0" <= character <= "9":
#         phone_number += character
#     else:
#         #FIXME: Add elif branches for letters and hyphen
#         phone_number += "?"

# print(f"Numbers only: {phone_number}")

# Third version
# user_input = input("Enter phone number: ")
# phone_number = ""

# for character in user_input:
#     if ("0" <= character <= "9") or (character == "-"):
#         phone_number += character
#     elif ("a" <= character <= "c") or ("A" <= character <= "C"):
#         phone_number += "2"
#     elif("d"<= character <="f") or ("D"<= character <="F"):
#         phone_number+="3"
#     elif("g"<= character <="i") or ("G"<= character <="I"):
#         phone_number+="4"
#     elif("j"<= character <="l") or ("J"<= character <="L"):
#         phone_number+="5"
#     elif("m"<= character <="o") or ("M"<= character <="O"):
#         phone_number+="6"
#     elif("p"<= character <="s") or ("P"<= character <="S"):
#         phone_number+="7"
#     elif("t"<= character <="v") or ("T"<= character <="V"):
#         phone_number+="8"
#     elif("w"<= character <="z") or ("W"<= character <="Z"):
#         phone_number+="9"       
#     #FIXME: Add remaining elif branches
#     else:
#         phone_number += "?"

# print(f"Numbers only: {phone_number}")


# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")   

# Example 2: Using enumerate with a string
# word = "hello"
# for index, char in enumerate(word):
#     print(f"Index: {index}, Character: {char}")

# colors = ["red", "green", "blue"]
# for index, color in enumerate(colors, start=1):
#     print(f"Position: {index}, Color: {color}")

# numbers = [10, 20, 30, 40]
# for index, value in enumerate(numbers):
#     numbers[index] = value * 2  # Double each number in the list
# print(numbers)  # Output: [20, 40, 60, 80]

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