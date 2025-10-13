""" Read in first equation, ax + by = c """
a = int(input())
b = int(input())
c = int(input())

""" Read in second equation, dx + ey = f """
d = int(input())
e = int(input())
f = int(input())

found = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f):
            print(f"x = {x} , y = {y}")
            found = True
            break
    if found:
        break
if not found:
    print("There is no solution")