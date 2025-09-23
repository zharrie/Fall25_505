# Strings and String Slicing
"""
Strings are sequences of characters, ordered by index from left to right. Each character has a numeric index, starting at 0. For example, my_str[5] accesses the sixth character of my_str.
To access multiple characters, Python uses slice notation:
my_str[start:end] → returns characters from index start up to, but not including, end.
Example: If my_str = "Boggle", then my_str[0:3] produces "Bog".
Examples
my_str = "John Doe"
my_str[0:4] → "John" (indices 0–3, excluding index 4).
my_str[4:7] → " Do".
my_str[5:8] or my_str[5:10] → "Doe".
Negative indices count from the end of the string.
Example: if my_str = "Jane Doe!?", then my_str[0:-2] → "Jane Doe" (up to the second-to-last character).
Slicing always creates a new string object. Changing the original string does not affect slices.
Omitting Indices
my_str[:end] → from index 0 up to end - 1.
my_str[start:] → from start through the end.
Example: my_str[:5] → characters 0–4; my_str[5:] → everything from index 5 onward.
Edge Cases
my_str[2:1] → "" (empty string, since start > end).
If end exceeds string length, slicing goes to the string’s actual end.
Variables can be used as slice indices: my_str[x:y].
Common Slicing Patterns
Given my_str = "http://en.wikipedia.org/wiki/Nasa/":
Syntax	Result	Description
my_str[10:19]	"wikipedia"	Characters 10–18.
my_str[10:-5]	"wikipedia.org/wiki/"	Characters 10 through -6.
my_str[8:]	"n.wikipedia.org/wiki/Nasa/"	From index 8 to the end.
my_str[:23]	"http://en.wikipedia.org"	Characters 0–22.
my_str[:-1]	"http://en.wikipedia.org/wiki/Nasa"	All but the last character.
Slice Stride
Slicing accepts an optional third argument, the stride, which sets the step size.
Example: my_str[0:10:2] → every second character from index 0 to 9.
Default stride is 1.
"""
my_str = "http://en.wikipedia.org/wiki/Nasa/"
print(my_str[10:19])  # "wikipedia"
print(my_str[10:-5])  # "wikipedia.org/wiki/"
print(my_str[8:])     # "n.wikipedia.org/wiki/Nasa/"
print(my_str[:23])    # "http://en.wikipedia.org"
print(my_str[:-1])    # "http://en.wikipedia.org/wiki/Nasa"
print(my_str[0:10:2]) # "h:/nwk"print(my_str[::3])    # "h:/eia.o/wsa"
print(my_str[::3])    # "h:/eia.o/wsa"
print(my_str[::-1])   # "/asaN/ikliw/gro.aidepikiw.ne//:ptth"
print(my_str[20:10:-1]) # "igapidew"
print(my_str[10:20:-1]) # "" (empty string, since start > end)

# Advanced string formatting
"""
A format specification can define a field width, which sets the minimum number of characters used to display a value. If the value is shorter than the specified width, padding is added (by default, spaces). For example, {name:16} ensures that the string in name takes up 16 characters of space.
Default alignment:
Numbers → right-aligned.
Strings (and most other types) → left-aligned.
Alignment can be explicitly controlled using special characters placed before the width:
< → left-align
> → right-align
^ → center-align
Padding is handled by a fill character, which precedes the alignment symbol. By default, this is a space " ". A different fill character can be specified.
Example:
{score:0>4} → "0009" if score = 9; "0250" if score = 250.
Examples:
Format Spec	    Value of score	    Output
{score:}	        9	                9
{score:4}	        9	                9
{score:0>4}	        9	                0009
{score:0>4}	        18	                0018
{score:0^4}	        18	                0180


Floating-Point Precision
The precision component of a format specification controls how many digits appear to the right of the decimal point in floating-point numbers. Precision is written after a period (.) following the width, if a width is given.
Example: f"{1.725:.1f}" → "1.7" (one digit after the decimal).
If precision is larger than the number of available digits, trailing zeros are added.
f"{1.5:.3f}" → "1.500".
If precision is smaller, the value is rounded.
f"{1.666:.2f}" → "1.67".
"""
score = 9
print(f"{score:}")      # "9"
print(f"{score:4}")     # "   9"
print(f"{score:0>4}")   # "0009"
print(f"{score:0>4}")   # "0018" (if score = 18)
print(f"{score:0^4}")   # "0180" (if score = 18)    
print(f"{1.725:.1f}")   # "1.7"
print(f"{1.5:.3f}")     # "1.500"
print(f"{1.666:.2f}")   # "1.67"

# String methods
"""
Strings are immutable objects but provide many built-in methods for searching, replacing, transforming, and comparing text. Each method creates and returns a new string rather than modifying the original.

Finding and Replacing
replace(old, new) → returns a copy with all occurrences of old replaced by new.
replace(old, new, count) → replaces only the first count occurrences.
find(x) → index of the first occurrence of x, or -1 if not found.
find(x, start[, end]) → search starting at start (and stopping before end).
rfind(x) → like find, but searches from the end.
count(x) → number of times x appears.

Use in for membership checks if the exact index isn’t needed:
if "batman" in superhero_name: ...

Comparing Strings
Strings can be compared using:
Relational/equality operators (<, >, ==, !=, etc.)
Membership operators (in, not in)
Identity operators (is, is not)

Comparison is case-sensitive and based on ASCII/Unicode values:
"Apple" < "apple" because "A" (65) < "a" (97).
"Yankee Sierra" > "Amy Wise" because "Y" (89) > "A" (65).

⚠️ Common mistake: using is instead of == for equality. is checks object identity, not value.

Boolean String Tests
Return True or False:
isalnum() → letters/numbers only
isdigit() → digits only
islower() / isupper() → all cased letters lower/upper
isspace() → whitespace only
startswith(x) / endswith(x) → prefix/suffix check

Creating New Strings
Useful for normalization (e.g., handling inconsistent user input):
capitalize() → first letter uppercase, rest lowercase
lower() → all lowercase
upper() → all uppercase
strip() → remove leading/trailing whitespace
title() → capitalize first letter of each word

Example for input normalization:
name = input().strip().lower()
This ensures "Bob", "BOB", or "bob" are all treated as "bob".

Best Practice
Apply transformations (e.g., stripping whitespace, case conversion) immediately when reading user input. This reduces bugs caused by inconsistent formatting—though in some contexts (e.g., passwords, case-sensitive data), preserving capitalization may be necessary.
"""
# Example: Simple guessing game
word = "onomatopoeia"
num_guesses = 10

hidden_word = "-" * len(word)

guess = 1

while guess <= num_guesses and "-" in hidden_word:
    print(hidden_word)
    user_input = input(f"Enter a character (guess #{guess}): ")

    if len(user_input) == 1:
        # Count the number of times the character occurs in the word
        num_occurrences = word.count(user_input)

        # Replace the appropriate position(s) in hidden_word with the actual character.
        position = -1
        for occurrence in range(num_occurrences):
            position = word.find(user_input, position +
                                 1)  # Find the position of the next occurrence
            hidden_word = (hidden_word[:position] + user_input +
                           hidden_word[position + 1:]
                           )  # Rebuild the hidden word string

        guess += 1

if not "-" in hidden_word:
    print("Winner!", end=" ")
else:
    print("Loser!", end=" ")

print(f"The word was {word}.")    

# Example: String methods
s = "  Hello, World!  "
print(s.replace("World", "Python"))  # "  Hello, Python!  "
print(s.find("o"))                    # 4
print(s.rfind("o"))                   # 8
print(s.count("l"))                   # 3
print("World" in s)                   # True
print(s == "  Hello, World!  ")       # True
print(s.isalnum())                    # False
print(s.isdigit())                    # False
print(s.islower())                    # False
print(s.isspace())                    # False
print(s.startswith("  He"))           # True
print(s.endswith("!  "))              # True
print(s.capitalize())                 # "  hello, world!  "
print(s.lower())                      # "  hello, world!  "
print(s.upper())                      # "  HELLO, WORLD!  "
print(s.strip())                      # "Hello, World!" 

# Splitting and joining strings
"""
The split() Method
The split() method breaks a string into a list of substrings, called tokens. A separator determines where the string is divided.
By default, split() uses whitespace as the separator:
"Martin Luther King Jr.".split()
# → ["Martin", "Luther", "King", "Jr."]

A custom separator can be specified:
"a#b#c".split("#")
# → ["a", "b", "c"]

For example, splitting a URL on / divides it into path components:
"http://en.wikipedia.org/wiki/Lucille_ball".split("/")
# → ["http:", "", "en.wikipedia.org", "wiki", "Lucille_ball"]

Notice:
Consecutive or trailing separators create empty string tokens ("").
With the default whitespace separator, empty strings are not generated.


The join() Method
The join() method does the reverse: it concatenates a list of strings into one string, inserting a chosen separator between elements.
"@".join(["billgates", "microsoft"])
# → "billgates@microsoft"

The separator can be any string, including multiple characters or even an empty string:
"".join(["http://", "www.", "ebay", ".com"])
# → "http://www.ebay.com"

Combining split() and join()
Together, these methods allow flexible editing of strings:
Changing separators:
"C:/Users/Brian/report.txt".split("/")
# → ["C:", "Users", "Brian", "report.txt"]
"\\".join(["C:", "Users", "Brian", "report.txt"])
# → "C:\\Users\\Brian\\report.txt"

Editing tokens:
Suppose a Wikipedia URL should contain "wiki" as the fourth token:
parts = "http://en.wikipedia.org/topic".split("/")
if parts[3] != "wiki":
    parts.insert(3, "wiki")
corrected = "/".join(parts)

"""
url = "http://en.wikipedia.org/topic"
parts = url.split("/")
if parts[3] != "wiki":
    parts.insert(3, "wiki")
corrected = "/".join(parts)
print(corrected)  # "http://en.wikipedia.org/wiki/topic"
print("Martin Luther King Jr.".split())  # ["Martin", "Luther", "King", "Jr."]
print("a#b#c".split("#"))  # ["a", "b", "c"]
print("http://en.wikipedia.org/wiki/Lucille_ball".split("/"))
# ["http:", "", "en.wikipedia.org", "wiki", "Lucille_ball"]
print("@".join(["billgates", "microsoft"]))  # "billgates@microsoft"
print("".join(["http://", "www.", "ebay", ".com"]))  # "http://www.ebay.com"    
print("C:/Users/Brian/report.txt".split("/"))
# ["C:", "Users", "Brian", "report.txt"]
print("\\".join(["C:", "Users", "Brian", "report.txt"]))
# "C:\\Users\\Brian\\report.txt"    