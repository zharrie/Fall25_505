full_name = input().split()

#For 3-part names
if len(full_name) == 3:
    first, middle, last = full_name
    print(f"{last}, {first[0]}.{middle[0]}.")

#For 2-part names
elif len(full_name) == 2:
    first, last = full_name
    print(f"{last}, {first[0]}.")