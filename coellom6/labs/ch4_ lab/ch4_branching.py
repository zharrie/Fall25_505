#4.17 LAB: Exact change 
change = int(input())

if change <= 0:
    print("No change") 
else: 
    coin_data = [
        ('Dollar', 'Dollars', 100), 
        ('Quarter', 'Quarters', 25),
        ('Dime', 'Dimes', 10),
        ('Nickel', 'Nickels', 5), 
        ('Penny', 'Pennies', 1),
    ]

    for singular, plural, value in coin_data:
        count = change // value  
        if count > 0: 
            if count == 1:
               print(f" {count} {singular}")
            else:
                print(f"{count} {plural}")
            change -= value * count

#4.18 LAB: Leap year

is_leap_year = False

input_year = int(input())

if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    print(f"{input_year} - leap year") 
else: 
    print(f"{input_year} - not a leap year")

#4.19 LAB: Golf scores

strokes = int(input()) 
par = int(input()) 

score_name = ""

if par in [3, 4, 5]: 
    if strokes == par -2:
        score_name = "Eagle" 
    elif strokes == par - 1:
        score_name = "Birdie" 
    elif strokes == par: 
        score_name = "Par"
    elif strokes == par + 1: 
        score_name = "Bogey" 
    else: 
        score_name = "Error" 
else: 
    score_names = "Error" 
print(f"Par {par} in {strokes} strokes is { score_name}")

#4.20 FizzBuzz Game

#Write the code to generate fizz when the number is divisible by 3, 
# buzz when the number is divisible by 5,
# cont- and fizzbuzz when the number is divisible by 15.

for num in range(1,101): 
    if num % 15 == 0: 
      print("fizzbuzz") 
    elif num % 3 == 0: 
      print("fizz") 
    else: 
      print(num) 





