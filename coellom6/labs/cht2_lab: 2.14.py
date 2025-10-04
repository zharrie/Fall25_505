# Lab: Divide Input Integers 
user_num=int(input())
div_num=int(input())

user_num = user_num // div_num
print(user_num, end=' ')

user_num = user_num // div_num
print(user_num, end=' ')

user_num = user_num // div_num
print(user_num)

# 2.15 LAB: Driving costs
miles_per_gallon = float(input())
dollars_per_gallon = float(input())

cost_20 = (20 / miles_per_gallon) * dollars_per_gallon
cost_75 = (75 / miles_per_gallon) * dollars_per_gallon
cost_500 = (500 / miles_per_gallon) * dollars_per_gallon

print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")

# 2.16 LAB: Expression for calories burned during workout
age = int(input())
weight = float(input())
heart_rate = float(input())
time = float(input()) 

calories = (( age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368

print(f"Calories: {calories:.2f} calories")

#2.17 LAB: Using math functions
import math

x = float(input())
y = float(input())
z = float(input())

value1 = x ** z 
value2 = x ** (y ** z)
value3 = abs(x - y) 
value4 = math.sqrt(x ** z)

print(f"{value1:.2f} {value2:.2f} {value3:.2f} {value4:.2f}")

#2.18 LAB: Musical note frequencies
import math 

f0 = float(input())
r = math.pow(2, 1/12)

print(f"{f0:.2f} Hz")
print(f"{f0 * r:.2f} Hz")
print(f"{f0 * r**2:.2f} Hz")
print(f"{f0 * r**3:.2f} Hz")

#2.19 LAB: Convert to dollars
nickels = int(input())
dimes = int(input())
quarters = int(input())

dollars = (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
print(f"Amount: ${dollars:.2f}")