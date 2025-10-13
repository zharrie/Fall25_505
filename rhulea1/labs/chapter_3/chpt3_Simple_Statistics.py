num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

#Compute product and average
product = (num1 * num2 * num3 * num4)
average = (num1 + num2 + num3 + num4) / 4

#output as integer
print(f"{product:.0f} {average:.0f}")

#output as floating-point
print(f"{product:.3f} {average:.3f}")
