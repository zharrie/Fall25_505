is_leap_year = False

input_year = int(input())

if input_year % 400 == 0 and input_year % 100 == 0:
    print(f"{input_year} - leap year")
elif input_year % 4 == 0 and input_year % 100 == 0:
    print(f"{input_year} - not a leap year")
elif input_year % 4 == 0 and not input_year % 100 == 0:
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")
    