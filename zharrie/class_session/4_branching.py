"""
In a program, a branch is a sequence of statements only executed under a certain condition. 
Ex: A hotel may discount a price only for people over age 65. 
An if branch is a branch taken only if an expression is true.
An if-else branch has two branches: 
The first branch is executed if an expression is true, else the other branch is executed.

Commonly a programmer wishes to take one of multiple (three or more) branches. 
An if-else can be extended to an if-elseif-else structure. 
Each branch's expression is checked in sequence; as soon as one branch's expression is found to be true, that branch is taken. 
If no expression is found true, execution will reach the else branch, which then executes.

Note: The else part is optional. If omitted, then if none of the previous expressions are true, no branch executes.

An if statement executes a group of statements if an expression is true. The statements in a branch must be indented, typically four spaces.

The example below uses ==. The equality operator (==) evaluates to True if the left and right sides are equal. Ex: If num_years is 50, then num_years == 50 evaluates to true. Note the equality operator is ==, not =.
"""

age = int(input("Enter age: "))
if age >= 65:
    print("You get the senior discount.")
    hotel_rate = hotel_rate * 0.9  # 10% discount
else:
    print("You do not get the senior discount.")
print(f"Your hotel rate: ${hotel_rate:.2f}")
# Output if input is 70
# You get the senior discount.
# Your hotel rate: $67.50
# Output if input is 40
# You do not get the senior discount.
# Your hotel rate: $75.00

if True:
    print("This line is printed because the expression is true.")
# Output: This line is printed because the expression is true.  
# If the expression is false, nothing is printed.

hotel_rate = 150
num_years = int(input("Enter years married: "))

if num_years == 50:
   print("Congratulations on 50 years of marriage!")
   hotel_rate = hotel_rate / 2

print(f"Your hotel rate: ${hotel_rate:.2f}")
# Output if input is 50
# Congratulations on 50 years of marriage!
# Your hotel rate: $75.00
# Output if input is not 50
# Your hotel rate: $150.00  

num_years = int(input("Enter years married: "))
if num_years == 50:
    print("Congratulations on 50 years of marriage!")
    hotel_rate = hotel_rate / 2
elif num_years >= 25:
    print("Congratulations on 25 years of marriage!")
    hotel_rate = hotel_rate * 0.75  # 25% discount
else:
    print("You do not get a discount.")
print(f"Your hotel rate: ${hotel_rate:.2f}")
# Output if input is 50
# Congratulations on 50 years of marriage!
# Your hotel rate: $75.00
# Output if input is 30
# Congratulations on 25 years of marriage!
# Your hotel rate: $112.50
# Output if input is 10
# You do not get a discount.
# Your hotel rate: $150.00  


"""
Equality and inequality operators

Whereas the equality operator checks whether two values are equal, the inequality operator (!=) evaluates to True if the left and right sides are not equal, or different.

An expression involving an equality or inequality operator evaluates to a Boolean value. A Boolean is a type that has just two values: True or False.
The relational operators <, <=, >, and >= evaluate to True or False.
Ex: 3 < 5 evaluates to True, and 3 >= 5 evaluates to False.
"""
num_guests = int(input("Enter number of guests: "))
if num_guests < 1:
    print("You must have at least one guest.")
elif num_guests > 6:
    print("You cannot have more than 6 guests.")
else:
    print("Your reservation is confirmed.")
# Output if input is 0
# You must have at least one guest.
# Output if input is 8
# You cannot have more than 6 guests.
# Output if input is 4
# Your reservation is confirmed.    

"""
Relational operators

A relational operator checks how one operand's value relates to another, such as being greater than.

Some operators, such as >=, involve two characters. A programmer cannot arbitrarily combine the >, =, and < symbols; only the two-character sequences shown represent valid operators.
Operator    Meaning
==          Equal to
!=          Not equal to
<           Less than
<=          Less than or equal to
>           Greater than
>=          Greater than or equal to    
Note: The equality operator (==) is different from the assignment operator (=). The assignment operator stores a value in a variable. The equality operator checks whether two values are equal.
"""

"""
Logical operators 
A logical operator treats operands as being True or False, and evaluates to True or False. 
Logical operators include AND, OR, and NOT. Programming languages typically use various symbols for those operators, but below the words AND, OR, and NOT are used for introductory purposes.

The and operator evaluates to True if both expressions are True. Ex: (3 < 5) and (4 < 6) evaluates to True.
The or operator evaluates to True if either expression is True. Ex: (3 < 5) or (4 > 6) evaluates to True.
The not operator negates an expression. Ex: not(3 < 5) evaluates to False.

a AND b	Logical AND: True when both of its operands are True.
a OR b	Logical OR: True when at least one of its two operands are True.
NOT a	Logical NOT: True when its one operand is False, and vice versa.
"""
age = int(input("Enter age: "))
if age >= 0 and age <= 120:
    print("Valid age.")
else:
    print("Invalid age.")
# Output if input is 30
# Valid age.
# Output if input is -5
# Invalid age.
# Output if input is 130
# Invalid age.

"""
Operator chaining

Python supports operator chaining. For example, a < b < c determines whether b is greater-than a but less-than c. Chaining performs comparisons left to right, evaluating a < b first. If the result is True, then b < c is evaluated next. If the result of the first comparison a < b is False, then there is no need to continue evaluating the rest of the expression. Note that a is not compared to c.
if age >= 0 and age <= 120:
can be written as
if 0 <= age <= 120:
"""
age = int(input("Enter age: "))
if 0 <= age <= 120:
    print("Valid age.")
else:
    print("Invalid age.")

"""
Booleans and logical operators

A Boolean refers to a value that is either True or False. 
Note that True and False are keywords in Python and must be capitalized. A programmer can assign a Boolean value by specifying True or False, or by evaluating an expression that yields a Boolean. 

a and b	Boolean AND: True when both operands are True.
a or b	Boolean OR: True when at least one operand is True.
not a	Boolean NOT (opposite): True when the single operand is False (and False when operand is True)
"""
is_raining = True
num_guests = 3
if is_raining:
    print("Take an umbrella.")
if not is_raining:
    print("No umbrella needed.")        
if is_raining and (num_guests > 0):
    print("Take an umbrella and welcome your guests.")  

if is_raining or (num_guests > 0):
    print("Either take an umbrella or welcome your guests.")
if not is_raining and (num_guests > 0):
    print("Welcome your guests; no umbrella needed.")

"""
Examples

Given age = 19, days = 7, user_char = "q"

(age > 16) and (age < 25)	True, because both operands are True.
(age > 16) and (days > 10)	False, because both operands are not True (days > 10 is False).
(age > 16) or (days > 10)	True, because at least one operand is True (age > 16 is True).
not (days > 10)	True, because operand is False.
not (age > 16)	False, because operand is True.
not (user_char == "q")	False, because operand is True.
"""

"""
Basic ranges with gaps

Ranges contain gaps. Ex: Movie theaters give ticket discounts to children (anyone 12 and under) and seniors (anyone 65 and older). The gap is the group of people aged 13 to 64. An if-else statement can be used to detect such ranges with gaps.
"""
age = int(input("Enter age: "))
if age <= 12:
    print("Child ticket price.")
elif age >= 65:
    print("Senior ticket price.")
else:
    print("Adult ticket price.")
# Output if input is 10
# Child ticket price.
# Output if input is 70
# Senior ticket price.
# Output if input is 30
# Adult ticket price.   

"""
Ranges with gaps using logical operators

Programmers often use logical operators to explicitly detect ranges with an upper and lower bound, including ranges with gaps that may have intermediate bounds. Ex: If a valid office number is within the ranges of 100 to 150 or 200 to 250, the logical AND operator or operator chaining can be used to identify the lower and upper bounds of the two ranges. Further, the ranges can be combined into a single branch using the logical OR operator.
"""
office_number = int(input("Enter office number: "))
if (100 <= office_number <= 150) or (200 <= office_number <= 250):
    print("Valid office number.")
else:
    print("Invalid office number.") 

"""
Nested if-else statements

A branch's statements can include any valid statements, including another if-else statement, which are known as nested if-else statements.

Ex: A hotel may give a senior discount only if the guest is a member of the hotel's loyalty program. The outer if statement checks whether the guest is a senior, and the inner if statement checks whether the guest is a loyalty program member.
"""
age = int(input("Enter age: "))
is_loyalty_member = input("Are you a loyalty program member (y/n)? ")
if age >= 65:
    if is_loyalty_member == "y":
        print("You get the senior loyalty discount.")
        hotel_rate = hotel_rate * 0.8  # 20% discount
    else:
        print("You get the senior discount.")
        hotel_rate = hotel_rate * 0.9  # 10% discount
else:
    print("You do not get the senior discount.")
print(f"Your hotel rate: ${hotel_rate:.2f}")

# Output if input is 70 and 'y' for loyalty     
# You get the senior loyalty discount. 
# Your hotel rate: $60.00
# Output if input is 70 and 'n' for loyalty
# You get the senior discount.
# Your hotel rate: $67.50
# Output if input is 40
# You do not get the senior discount.
# Your hotel rate: $75.00   

"""
Comparing data types and common errors

A common error is to compare values of different data types. Ex: A programmer may wish to check whether a character variable user_char contains the letter "q". If user_char is a string, then the expression user_char == "q" evaluates to True if user_char contains "q", and False otherwise. However, if user_char is a number, then the expression user_char == "q" always evaluates to False, because a number can never equal a string.
Note: A programmer can use the type function to determine a variable's data type. Ex: type(user_char) returns str if user_char is a string, and int if user_char is an integer.
Another common error is to use = rather than == in an if-else expression, as in: if numDogs = 9:. In such cases, the interpreter should generate a syntax error.
Another common error is to use invalid character sequences like =>, !<, or <>, which are not valid operators.
"""
user_char = input("Enter a character: ")
if user_char == "q":
    print("You entered the letter q.")
else:
    print("You did not enter the letter q.")

"""
Membership operators: in/not in

One programming task involves determining whether a specific value can be found within a container, such as a list or dictionary. The in and not in operators, known as membership operators, yield True or False if the left operand matches the value of an element in the right operand, which is always a container.
The membership operators can be used with sequence types. If the variable x is a list or tuple, then a in x evaluates to True if there exists an index idx for which a == x[idx] is True.
Ex: If lst = [3, 1, 4, 1, 5, 9], then 3 in lst evaluates to True because lst[0] == 3 is True. However, 2 in lst evaluates to False because there is no index idx for which lst[idx] == 2 is True.
Membership operators can be used to check whether a string is a substring, or matching subset of characters, of a larger string. For example, "abc" in "123abcd" returns True because the substring abc exists in the larger string.
Ex: If lst = [3, 1, 4, 1, 5, 9], then 3 in lst evaluates to True, but 2 in lst evaluates to False.
Ex: If s = "abcdef", then "abc" in s evaluates to True, but "acb" in s evaluates to False.
Membership in a dictionary (dict) implies that a specific key exists in the dictionary. A common error is to assume that a membership operator checks the values of each dictionary key as well.
Ex: If d = {"a": 1, "b": 2, "c": 3}, then "a" in d evaluates to True, but 1 in d evaluates to False.
"""

"""
Identity operators: is/is not

Sometimes a programmer wants to determine whether two variables are the same object. The programmer can use the identity operator, is, to check whether two operands are bound to a single object. The inverse identity operator, is not, gives the negated value of "is". Thus, if x is y is True, then x is not y is False.

Identity operators do not compare object values; rather, identity operators compare object identities to determine equivalence. Object identity is usually the memory address of an object. Thus, identity operators return True only if the operands reference the same object.

A common error is to confuse the equivalence operator "==" and the identity operator "is" because a statement such as if x is 3 is valid syntax and is grammatically appealing. Python may confusedly evaluate the statement x is 3 as True, but y is 1000 as False, when x = 3 and y = 1000. Python interpreters typically precreate objects for a small range of numbers to avoid constantly recreating objects for such small values. In the example above, an object for 3 was precreated, so x references the same object as the literal. However, Python did not precreate an object for 1000. A good practice is to avoid using the identity operators "is" and "is not", unless explicitly testing whether two objects are identical.

The id() function can be used to retrieve the identifier of any object. If x is y is True, then id(x) == id(y) is also True.
"""
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)        # True, because y references the same object as x
print(x is z)        # False, because z references a different object with the same value
print(x == z)        # True, because x and z have the same value
print(id(x), id(y), id(z))  # id(x) == id(y), but id(x) != id(z)

"""
Precedence rules

The order in which operators are evaluated in an expression is known as precedence rules. Arithmetic, logical, and relational operators are evaluated in the order shown below.
Precedence	Operators
Highest	Parentheses ( )
Next	Exponentiation **
Next	Unary +, - (plus and minus signs)
Next	Multiplication *, Division /, Floor division //, Modulus %
Next	Addition +, Subtraction -
Next	Relational operators: <, <=, >, >=     
Next	Equality operators: ==, !=  
Next	Logical NOT
Next	Logical AND
Lowest	Logical OR
Operators with higher precedence are evaluated before operators with lower precedence. Operators with the same precedence are evaluated left to right. Parentheses can be used to change the order of evaluation.
"""
"""
Common error: Missing parentheses

A common error is to write an expression that is evaluated in a different order than expected. Good practice is to use parentheses in expressions to make the intended order of evaluation explicit. For example, a programmer might write:

not a == b intending to mean (not a) == b, but the interpreter computes not (a == b) because equality operators (==) have precedence over logical operations (not).
w and x == y and z intending (w and x) == (y and z), but the interpreter computes (w and (x == y)) and z because == has precedence over and.
not x + y < 5 intending (not x) + y < 5, but the interpreter computes not ((x + y) < 5) because the addition operator + has the highest precedence and is computed first, followed by the relational operation <, and finally the logical not operation.
"""

"""
Conditional expressions
A conditional expression has the following form: expr_when_true if condition else expr_when_false
The condition is evaluated first. If the condition is True, then expr_when_true is evaluated and returned; otherwise, expr_when_false is evaluated and returned. A conditional expression is similar to an if-else statement, but a conditional expression can be used within another expression. A common use of a conditional expression is to assign a value to a variable based on a condition.
A conditional expression has three operands and thus is sometimes referred to as a ternary operation.
"""
age = int(input("Enter age: "))
hotel_rate = 150
hotel_rate = hotel_rate * 0.9 if age >= 65 else hotel_rate
print(f"Your hotel rate: ${hotel_rate:.2f}")
# Output if input is 70
# Your hotel rate: $135.00
# Output if input is 40
# Your hotel rate: $150.00  