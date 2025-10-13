""" Read in first equation, ax + by = c """
a = int(input())
b = int(input())
c = int(input())

""" Read in second equation, dx + ey = f """
d = int(input())
e = int(input())
f = int(input())

solution_x = 0
solution_y = 0

solution_found = False
for x in range(-10,11):
    for y in range(-10,11):
        if (a * x + b * y == c) and (d * x + e * y == f):
            solution_found = True
            solution_x = x
            solution_y = y
            break
    if solution_found:
        break
        
    
if solution_found:
    print(f"x = {solution_x} , y = {solution_y}")
else:
    print("There is no solution")