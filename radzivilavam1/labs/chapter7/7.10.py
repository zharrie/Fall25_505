""" Type your code here. """
input_str = str(input())

new_str = ''
for char in input_str:
    if char.isalpha():
        new_str += char
print(new_str)