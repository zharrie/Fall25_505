age=int(input())
weight = int(input())
heart=int(input())
time=int(input())
calories = (((age * 0.2757) + (weight * 0.03295) + (heart * 1.0781) - 75.4991) * time) / 8.368
print(f"calories:{calories:.2f}, calories")




