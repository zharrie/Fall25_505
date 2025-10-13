count = int(input())

values = []
for _ in range(count):
    values.append(float(input()))

max_val = max(values)  # largest value

for v in values:
    print(f"{v / max_val:.2f}")
