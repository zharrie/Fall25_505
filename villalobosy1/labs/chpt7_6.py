full_name = input()
names = full_name.split()

if len(names) == 3:
    print(f"{names[2]}, {names[0][0]}.{names[1][0]}.")

elif len(names) == 2:
    print(f"{names[1]}, {names[0][0]}.")
