# Define your function here.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    dollar_cost = ((miles_driven / miles_per_gallon) * dollars_per_gallon)
    print(f"{dollar_cost:.2f}")
    return dollar_cost


if __name__ == "__main__":
    # Type your code here.
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven=10)
    driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven=50)
    driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven=400)