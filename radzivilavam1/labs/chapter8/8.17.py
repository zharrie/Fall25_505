""" Type your code here. """
input_list = [int(i) for i in str(input()).split()]
input_list = [i for i in input_list if i < 0]

for v in sorted(input_list, reverse=True):
    print(v, end=' ')