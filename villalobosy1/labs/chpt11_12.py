from datetime import date, timedelta, time

def read_date():
        date_str = input()
        format_d = date_str.split("-")
        year = int(format_d[0])
        month = int(format_d[1])
        day = int(format_d[2])
        return date(year, month, day)

if __name__ == "__main__":
    dates = []
    while len(dates) < 4:
        d = read_date()
        dates.append(d)
    sorted_dates = sorted(dates)

    for x in sorted_dates:
        print(x.strftime("%m/%d/%Y"))

    day_difference = abs((sorted_dates[-1] - sorted_dates[-2]).days)
    print(f"{day_difference}")

    future_date = sorted_dates[-1] + timedelta(weeks=3)
    print(future_date.strftime("%B %d, %Y"))
    
    print(sorted_dates[0].strftime("%A"))