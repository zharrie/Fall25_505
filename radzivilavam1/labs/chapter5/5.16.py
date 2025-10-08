int_1 = int(input())
int_2 = int(input())

if int_1 <= int_2:
    increment = int_1
    while increment <= int_2:
        print(f"{increment}", end=" ")
        increment += 5
    print()
else:
    print("Second integer can't be less than the first.")
