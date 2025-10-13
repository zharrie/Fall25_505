# Define your function here.
def int_to_reverse_binary(integer_value: int):
    binary_string = ""
    while integer_value > 0:
        binary_string += str(integer_value % 2)
        integer_value = integer_value // 2
    return binary_string

def string_reverse(input_string: str):
    rev_str = ""
    for n in reversed(input_string):
        rev_str += n
    print(rev_str)
    return rev_str


if __name__ == "__main__":
    binary_string = int_to_reverse_binary(int(input()))
    string_reverse(binary_string)
