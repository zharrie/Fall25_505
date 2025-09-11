age_years = int(input())
weight_lbs = int(input())
heart_rate = int(input())
time_min = int(input())
calories = ((age_years * 0.2757) + (weight_lbs * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time_min / 8.368
print(f"Calories: {calories:.2f} calories")