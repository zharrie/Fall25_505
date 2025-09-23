def int_to_reverse_binary(integer_value):
    reverse_binary = ''
    if integer_value == 0:
        return '0'
    while integer_value > 0:
        e = integer_value % 2
        reverse_binary += str(e)
        integer_value = integer_value //2 
    return reverse_binary
    

def string_reverse(input_string):
   return input_string[::-1]
if __name__ == "___main___":
    user_input = int(input())
    reversed_binary = int_to_reverse_binary(user_input)
    final_binary = string_reverse(reversed_binary)
    print(final_binary)