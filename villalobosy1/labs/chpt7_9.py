x = input()
x1 = x.replace(' ', '')
reversed_x = x1[::-1]

if reversed_x == x1:
    print(f"palindrome: {x}")
else:
    print(f"not a palindrome: {x}")