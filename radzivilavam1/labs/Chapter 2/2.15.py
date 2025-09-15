car_gas_mileage = float(input())
gas_cost = float(input())

print(f"{((20 / car_gas_mileage) * gas_cost):.2f} {((75 / car_gas_mileage) * gas_cost):.2f} {((500 / car_gas_mileage) * gas_cost):.2f}")