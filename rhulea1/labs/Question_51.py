def max_number(num1, num2, num3, num4)
def min_number(num1, num2, num3, num4)
#Assume num1 is the largest
maximum = num1
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3
    if num4 > maximum:
        maximum = num4
    return maximum

#Assume num1 is the smallest
minimum = num1
    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3
    if num4 < minimum:
        minimum = num4
    return minimum

#Read four integers from input
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

#Compute maximum and minimum
maximum = max_number(num1, num2, num3, num4)
minimum = min_number(num1, num2, num3, num4)

#Output results
print("Maximum is", maximum)
print("Minimum is", minimum)
