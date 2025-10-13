num_values = int(input())
values = []

for a in range(num_values):
    values.append(float(input()))

#Finding the max values
max_values = max(values)

#Normalize each value by dividing by max value
for value in values:
    normalized = value / max_values
    print(f"{normalized:.2f}")
