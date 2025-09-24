total_change = int(input())
penny = 1
nickel = 5
dime = 10
quarter = 25
dollar = 100

if total_change  == 0:
    print("No change")

else:
    dollars = total_change // dollar
    total_change %= dollar

    quarters = total_change // quarter
    total_change %= quarter

    dimes = total_change // dime
    total_change %= dime

    nickels = total_change // nickel
    total_change %= nickel

    pennies = total_change // penny

    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")