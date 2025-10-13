def int_to_reverse_binary(integer_value):
    if integer_value == 0:
    return "0"
    binary_str = ""
    while integer_value > 0:
        binary_str += str(integer_value % 2)
        integer_value = integer_value // 2
    return binary_strefine your functions here.

if __name__ == "__main__":
    def string_reverse(input_string):
    return input_string[::-1]

num = int(input())
rev_binary = int_to_reverse_binary(num)
binary = string_reverse(rev_binary)
print(binary)