class Car:
    def __init__(self, year=0, purchase_price=0):
        self.year = year
        self.purchase_price = purchase_price

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        car_age = current_year - self.year
        current_value = self.purchase_price * ((1 - depreciation_rate) ** car_age)
        return int(current_value)

    def print_info(self, current_year):
        print("Car's information:")
        print(f"  Model year: {self.year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.calc_current_value(current_year)}")


if __name__ == "__main__":
    year = int(input())
    price = int(input())
    current_year = int(input())

    my_car = Car(year, price)
    my_car.print_info(current_year)
