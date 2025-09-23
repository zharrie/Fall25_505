#5.15 LAB: Password modifier
word = input()
password = ""

for ch in word: 
    if ch == "i": 
        password += "1"
    elif ch == "a":
        password += "@"
    elif ch == "m": 
        password += "M" 
    elif ch == "B": 
        password += "8" 
    elif ch == "s": 
        password += "$"
    else: 
        password += ch 
password += "!" 
print(password) 

#5.17 LAB: Print string in reverse
while True: 
    user_input = input() 
    if user_input == "Done" or user_input == "done" or user_input == "d":
        break 
    print(user_input[::-1])

#5.18 LAB: Brute force equation solver
""" Read in first equation, ax + by = c """
a = int(input())
b = int(input())
c = int(input())

""" Read in second equation, dx + ey = f """
d = int(input())
e = int(input())
f = int(input())

for x in range(-10, 11): 
    for y in range(-10, 11):
        if (a * x + b * y == c) and (d * x + e * y == f) 
            print(f'x = {x}, y ={y}') 
            found = true 
            break
        if found:
            break
if not found: 
    print('There is no solution.')

#5.19 LAB: Adjust values in a list by normalizing
num_values = int(input())
values =[]

for _ in range(num_values): 
    values.append(float(input()))
max_value = max(values) 

for value in values: 
    print(f"{value / max_value:.2f}")
