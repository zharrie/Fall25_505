''' Type your code here. '''
nickels = int(input())
dimes = int(input())
quarters = int(input())

cents = (nickels*5) + (dimes*10) + (quarters*25)
dollars = cents / 100
print(f"Amount: ${dollars:.2f}")