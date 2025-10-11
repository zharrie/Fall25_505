""" Type your code here. """
input_list = [int(i) for i in input().split()]
bounds = [int(j) for j in input().split()]

for v in input_list:
    if bounds[0] <= v <= bounds[1]:
        print(v, end=',')