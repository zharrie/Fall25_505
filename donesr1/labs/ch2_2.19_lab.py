nickels = int(input())
dimes = int(input())
quarters = int(input())
total_cents = (nickels * 5) + (dimes * 10) + (quarters * 25)
dollars = total_cents // 100
cents = total_cents % 100
print(f"Amount: ${dollars}.{cents}")