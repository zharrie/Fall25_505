import math
x = float(input())
y = float(input())
z = float(input())
#Perform calcultion
output1 = math.pow(x, z)
output2 = math.pow(x, math.pow(y, z))
output3 = math.fabs(x-y)
output4 = math.sqrt(math.pow(x, z))
print(f"{output1:.2f} {output2:.2f} {output3:.2f} {output4:.2f}")