is_leap_year = False

input_year = int(input())

# Rule 1: Year must be divisible by 4
if (input_year % 4 == 0):
    # Rule 2: If it's a century year, it must also be divisible by 400
    if (input_year % 100 == 0) and (input_year % 400 != 0):
        print(f"{input_year} - leap year")
    else:
        print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")