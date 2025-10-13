val1 = int(input())
val2 = int(input())

if val2 >= val1:
    while val2 >= val1:
        print(val1, end= " ")
        val1 += 5
    print()
else:
    print("Second integer can\'t be less than the first.")
