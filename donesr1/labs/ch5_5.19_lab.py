
n = int(input())


values = []
for _ in range(n):
    values.append(float(input()))


max_val = max(values)

for v in values:
    adjusted = v / max_val
    print(f"{adjusted:.2f}")