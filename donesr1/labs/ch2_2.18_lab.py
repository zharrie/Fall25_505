import math
frequency = int(input())
n0 = 0
n1 = 1
n2 = 2
n3 = 3
r = math.pow(2,1/12)
fn_0 = frequency * math.pow(r,n0)
fn_1 = frequency * math.pow(r,n1)
fn_2 = frequency * math.pow(r,n2)
fn_3 = frequency * math.pow(r,n3)

print(f"{fn_0:.2f} Hz")
print(f'{fn_1:.2f} Hz')
print(f"{fn_2:.2f} Hz")
print(f"{fn_3:.2f} Hz")
