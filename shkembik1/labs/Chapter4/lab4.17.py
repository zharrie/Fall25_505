cents = int(input())

if cents == 0:
    print("No change")
else:
    dollars,  cents = divmod(cents, 100)
    quarters, cents = divmod(cents, 25)
    dimes,    cents = divmod(cents, 10)
    nickels,  cents = divmod(cents, 5)
    pennies         = cents

    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(f"{dollars} Dollars")

    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(f"{quarters} Quarters")

    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(f"{dimes} Dimes")

    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(f"{nickels} Nickels")

    if pennies == 1:
        print("1 Penny")
    elif pennies > 1:
        print(f"{pennies} Pennies")