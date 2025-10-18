x = int(input())
y = int(input())
z = int(input())

smallest = x

if y < smallest:
    smallest = y

if z < smallest:
    smallest = z

print(smallest)

