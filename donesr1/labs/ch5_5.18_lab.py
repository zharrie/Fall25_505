# Read coefficients
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

# Brute force search for integer solutions in range -10 to 10
solution_found = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            solution_found = True