gas_milage = float(input())
gas_cost = float(input())
cost_20 = 20 / gas_milage * gas_cost
cost_75 = 75 / gas_milage * gas_cost
cost_500 = 500 / gas_milage * gas_cost
print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")