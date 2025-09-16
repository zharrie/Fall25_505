nickels = int(input()) *0.05
dimes = int(input()) *0.10
quarters = int(input()) *0.25

dollars = nickels + dimes + quarters % 100

print(f"Amount: ${dollars:.2f}")