
def int_to_reverse_binary(integer_value):
    if integer_value == 0:
        return "0"
    bits = ""
    while integer_value > 0:
        bits += str(integer_value % 2)
        integer_value //= 2
    return bits

def string_reverse(input_string):
    rev = ""
    for i in range(len(input_string) - 1, -1, -1):
        rev += input_string[i]
    return rev

if __name__ == "__main__":

    x = int(input())
    rev_bits = int_to_reverse_binary(x)
    print(string_reverse(rev_bits))