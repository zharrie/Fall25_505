miles_per_gallon = float(input())
dollars_per_gallon = float(input())
distance1 = 20
distance2 = 75
distance3 = 500
#Calculate the costs
cost1 = (distance1 / miles_per_gallon) * dollars_per_gallon
cost2 = (distance2 / miles_per_gallon) * dollars_per_gallon
cost3 = (distance3 / miles_per_gallon) * dollars_per_gallon
print(f"{cost1:.2f} {cost2:.2f} {cost3:.2f}")