def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven= 10):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon


if __name__ == "__main__":
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    miles_driven = float(input())


total = driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)
print(f"{total:.2f}")