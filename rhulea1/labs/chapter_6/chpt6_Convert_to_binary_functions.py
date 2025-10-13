# Define your functions here.
def int_to_reverse_binary(integer_value):
    reverse_binary = ""
    while integer_value > 0:
        reverse_binary += str(integer_value % 2)
        integer_value = integer_value // 2
    return reverse_binary

#Function to reverse a string
def string_reverse(input_string):
    reverse_string = input_string[::-1]
    return reverse_string

if __name__ == "__main__":
    #Read a positive integer from input
    number = int(input())
    #Get the reversed binary string
    rev_binary = int_to_reverse_binary(number)
    #Reverse the string returned from
    binary = string_reverse(rev_binary)
    print(binary)