#Read total change amounts in cents
total_cents = int(input())

if total_cents <= 0:
    print("No change")
else:
# Define coins types as singular, plural and value
    coins = [
        ("Dollar", "Dollars", 100),
        ("Quarter", "Quarters", 25),
        ("Dime", "Dimes", 10),
        ("Nickel", "Nickels", 5),
        ("Penny", "Pennies", 1)
    ]
    #Loop through each coin
    for singular, plural, value in coins:
        count = total_cents // value
        total_cents = total_cents % value
        if count > 0:
         if count == 1:
            print(f"1 {singular}")
         else:
            print(f"{count} {plural}")
