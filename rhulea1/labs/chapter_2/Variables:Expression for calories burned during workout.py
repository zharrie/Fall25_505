age_years = int(input())
weight_pounds = int(input())
hrtbeat_per_minute = int(input())
time_minutes = int(input())
avg_calories = ((age_years * 0.2757) + (weight_pounds * 0.03295) + (hrtbeat_per_minute * 1.0781) - 75.4991) * time_minutes / 8.368
print(f"Calories: {avg_calories:.2f} calories")
