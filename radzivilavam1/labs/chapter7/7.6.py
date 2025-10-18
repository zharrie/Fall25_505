""" Type your code here. """
input_list = input().split(" ")

if len(input_list) == 3:
    print(f"{input_list[2]}, {input_list[0][0]}.{input_list[1][0]}.")
if len(input_list) == 2:
    print(f"{input_list[1]}, {input_list[0][0]}.")