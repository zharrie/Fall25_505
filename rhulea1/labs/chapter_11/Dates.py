from datetime import date, timedelta, time, datetime


# 1 Complete read_date()
def read_date():

#Read input string with yyyy-mm-dd format
    date_str = input().strip()

#Convert string to date object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    return date_obj

#Read four (unique) date objects, putting the date objects in a list
dates =[]
for i in range(4):
    dates.append(read_date())

#Sort the dates earliest first
sorted_dates = sorted(dates)

#Output the sorted_dates in order, earliest first, in the format mm/dd/yy
for i in sorted_dates:
    print(i.strftime("%m/%d/%Y"))

#Number of days between the last two dates 
date_diff = abs((sorted_dates[-1] - sorted_dates[-2]).days)
print(date_diff)

#Date 3 weeks from the most recent date in the list
three_weeks = sorted_dates[-1] + timedelta(weeks=3)
print(three_weeks.strftime("%B %d, %Y"))

#Day of the week of the earliest day
print(sorted_dates[0].strftime("%A"))