positive_int = int(input())
binary_list = []

while positive_int > 0:
    binary_list.append(positive_int % 2)
    positive_int = int(positive_int/2)

for i in binary_list:
    print(i, end="")

print()