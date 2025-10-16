change = int(input())
coins = [
    ("Dollar", 100),
    ("Quarter", 25),
    ("Dime", 10),
    ("Nickel", 5),
    ("Penny", 1)
]
for name, value in coins:
    count = change // value
    change %= value
    
    if count > 0:
        if count == 1:
            print(f"{count} {name}")
        else:
            if name == "Penny":
                print(f"{count} Pennies")
            else:
                print(f"{count} {name}s")