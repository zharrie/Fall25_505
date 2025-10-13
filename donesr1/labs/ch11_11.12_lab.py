from datetime import datetime, timedelta

def read_date():
    # Read input string and convert it to a date object
    date_str = input()
    return datetime.strptime(date_str, "%Y-%m-%d").date()

# Read 4 unique dates
dates = []
for _ in range(4):
    date = read_date()
    while date in dates:
        date = read_date()
    dates.append(date)

# Sort dates from earliest to latest
sorted_dates = sorted(dates)

# Output sorted dates in mm/dd/yyyy format (no labels)
for d in sorted_dates:
    print(d.strftime("%m/%d/%Y"))

# Output number of days between the last two dates
days_between = abs((sorted_dates[-1] - sorted_dates[-2]).days)
print(days_between)

# Output the date 3 weeks after the most recent date
future_date = sorted_dates[-1] + timedelta(weeks=3)
print(future_date.strftime("%B %d, %Y"))

# Output the full weekday name of the earliest date
print(sorted_dates[0].strftime("%A"))
