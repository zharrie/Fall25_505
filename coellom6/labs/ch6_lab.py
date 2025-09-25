#6.20 LAB: Step counter
# Define your function here 
def feet_to_steps(user_feet):
    return int(user_feet / 2.5)

if __name__ == "__main__":
   feet_walked = float(input())
   steps = feet_to_steps(feet_walked)
   print(steps)
    # Type your code here.
#6.21 LAB: Convert to binary - functions

def int_to_reverse_binary(integer_value):
    binary_string = ' ' 
    while integer_value > 0:
        remainder = integer_value % 2
        binary_string += str(remainder)
        integer_value = integer_value // 2
    return binary_string

def string_reverse(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    user_input = int(input())
    reverse_binary = int_to_reverse_binary(user_input)
    print(string_reverse(reverse_binary))
#6.22 LAB: Swapping variables
def swap_values(user_val1, user_val2, user_val3, user_val4): 
    return user_val2, user_val1, user_val4, user_val3

if __name__ == "__main__": 
   user_val1 = int(input())
   user_val2 = int(input()) 
   user_val3 = int(input())
   user_val4 = int(input())

   swapped1, swapped2, swapped3, swapped4 = swap_values(user_val1, user_val2, user_val3, user_val4)
   print(swapped1, swapped2, swapped3, swapped4)

#6.23 LAB: Fibonacci sequence
def fibonacci(n):
    if n < 0: 
        return -1 
    elif n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else:
        a,b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b 
        return b 

if __name__ == "__main__":
    start_num = int(input())
    print(f"fibonacci({start_num}) is {fibonacci(start_num)}")