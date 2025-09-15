import math
f0 = float(input())
r = math.pow(2, 1/12)

print(f"{f0:.2f} Hz")
print(f"{f0 * r:.2f} Hz")
print(f"{f0 * r* r:.2f} Hz")
print(f"{f0 * r * r *r:.2f} Hz")