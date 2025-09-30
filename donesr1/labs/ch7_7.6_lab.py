full_name = input()
first, middle, last = full_name.split()
print(f"{last}, {first[0]}.{middle[0]}.")