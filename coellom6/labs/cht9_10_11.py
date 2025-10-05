#9.11 LAB: Car value (classes)
class Car:

    def __init__(self):
        self.model_year = 0
        # TODO: Declare purchase_price attribute
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price *
                                   (1 - depreciation_rate)**car_age)

    # TODO: Define print_info() method to output model_year, purchase_price, and current_value
    def print_info(self):
        print("Car's information:")
        print(f'  Model year: {self.model_year}')
        print(f'  Purchase price: ${self.purchase_price}')
        print(f'  Current value: ${self.current_value}')  

if __name__ == "__main__":
    year = int(input())
    price = int(input())
    current_year = int(input())

    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()

#9.16 LAB: Vending machine
class VendingMachine:

    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print(f"Inventory: {self.bottles} bottles")


if __name__ == "__main__":
    # TODO: Create VendingMachine object
    # TODO: Purchase first input number of bottles of drinks
    # TODO: Restock second input number of bottles of drinks
    # TODO: Purchase last input number of bottles of drinks
    # TODO: Report inventory
    buy_1 = int(input())
    restock = int(input())
    buy_2 = int(input())

    machine = VendingMachine()
    machine.purchase(buy_1)
    machine.restock(restock)
    machine.purchase(buy_2)
    machine.report()

#10.9 LAB: Exceptions with lists
names = [
    "Ryley",
    "Edan",
    "Reagan",
    "Henry",
    "Caius",
    "Jane",
    "Guto",
    "Sonya",
    "Tyrese",
    "Johnny",
]
index = int(input())

try:
    print("Name:", names[index])
except IndexError as excpt:
    print(f"Exception! {excpt}")
    if index < 0:
        print(f"The closest name is: {names[0]}")
    else:
        print(f"The closest name is: {names[-1]}")

#10.10 LAB: Simple integer division - multiple exception handlers
try:
    user_num = int(input())
    div_num = int(input())
    print(user_num // div_num)
except ZeroDivisionError as excpt:
    print(f"Zero Division Exception: {excpt}")
except ValueError as excpt:
    print(f"Input Exception: {excpt}")

#10.12 LAB: Student info not found - custom exception types
# Define custom exception
class StudentInfoError(Exception):

    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    if name in info:
        return info[name]
    else:
        raise StudentInfoError(f"student name not found for {name}")
    
    
def find_name(ID, info):
    for name, student_id in info.iteams():
        if student_id == ID:
            return name
    raise StudentInfoError(f"student ID not found for", {ID})


if __name__ == "__main__":
    # Dictionary of student names and IDs
    student_info = {
        "Reagan": "rebradshaw835",
        "Ryley": "rbarber894",
        "Peyton": "pstott885",
        "Tyrese": "tmayo945",
        "Caius": "ccharlton329",
    }

    userChoice = (
        input())  # Read search option from user. 0: find_ID(), 1: find_name()

    # FIXME: find_ID() and find_name() may raise an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    if userChoice == "0":
        name = input()
        result = find_ID(name, student_info)
    else:
        ID = input()
        result = find_name(ID, student_info)
    print(result)
except StudentInforError as exc:
    print(exc.message)

#11.12 LAB: Dates
from datetime import date, timedelta, time
# 1 Complete read_date()
def read_date():
    date_str = input()
    y, m, d = map(int, date_str.split('-'))
    date_obj = date(y, m, d)
    return date_obj
    """Read a string representing a date in the format 2121-04-12, create a
    date object from the input string, and return the date object
    """
dates = []
for _ in range (4):
    d = read_date()
    dates.append(d)

sorted_dates = sorted(dates)

for d in sorted_dates:
    print(d.strftime("%m/%d/%Y"))

days_diff = (sorted_dates[-1] - sorted_dates[-2]).days
print(abs(days_diff))

three_weeks = sorted_dates[-1] + timedelta(weeks = 3)
print(three_weeks.strftime("%B %d, %Y"))

print(sorted_dates[0].strftime("%A"))