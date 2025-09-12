import math
f0 = int(input())
r = math.pow(2,1/12)

n = 1
f1 = f0 * math.pow(r, n)
f2 = f1 * math.pow(r, n)
f3 = f2 * math.pow(r, n)

print(f"{f0:.2f} Hz")
print(f"{f1:.2f} Hz")
print(f"{f2:.2f} Hz")
print(f"{f3:.2f} Hz")