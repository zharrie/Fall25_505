x = input()

y = ""

for char in x:
    if char.isalpha():
        y += char
print(y)