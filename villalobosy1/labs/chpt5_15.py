word = input()
password = ""

for character in word: 
    if character == "i":
        password += "1"
    elif character == "a":
        password += "@"
    elif character == "m":
        password += "M"
    elif character == "B":
        password += "8"
    elif character == "s":
        password += "$"
    else:
        password += character
print (password + '!')