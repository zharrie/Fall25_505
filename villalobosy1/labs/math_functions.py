import math
x = float(input())
y = float(input())
z = float(input())

val_1 = math.pow (x,z)
val_2 = (math.pow(x,(math.pow (y,z))))
val_3 = math.fabs(x - y)
val_4 = math.sqrt(math.pow(x,z))

print(f"{val_1:.2f} {val_2:.2f} {val_3:.2f} {val_4:.2f}")