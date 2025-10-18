change_amount = int(input())

if change_amount <= 0:
    print("No change")
else:
    remainder = change_amount % 100
    if change_amount >= 100:
        dollars_num = change_amount // 100
        if dollars_num == 1:
            print(f"{dollars_num} Dollar")
        else:
            print(f"{dollars_num} Dollars")

    if remainder >= 25:
        quarter_num = remainder // 25
        if quarter_num == 1:
            print(f"{quarter_num} Quarter")
        else:
            print(f"{quarter_num} Quarters")
        remainder = remainder - (quarter_num * 25)
    
    if remainder >= 10:
        dime_num = remainder // 10
        if dime_num == 1:
            print(f"{dime_num} Dime")
        else:
            print(f"{dime_num} Dimes")
        remainder = remainder - (dime_num * 10)
    
    if remainder >= 5:
        nickel_num = remainder // 5
        if nickel_num == 1:
            print(f"{nickel_num} Nickel")
        else:
            print(f"{nickel_num} Nickels")
        remainder = remainder - (nickel_num * 5)
    
    if remainder >= 1:
        penny_num = remainder // 1
        if penny_num == 1:
            print(f"{penny_num} Penny")
        else:
            print(f"{penny_num} Pennies")
    




