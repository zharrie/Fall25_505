# Define your function here.
def swap_values(user_val1, user_val2, user_val3, user_val4):
    #Swapping values, first with second and third with fourth
    return user_val2, user_val1, user_val4, user_val3

if __name__ == "__main__": 
    # Read four integers from input
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())

    #Call the function to swap
    swapped1, swapped2, swapped3, swapped4 = swap_values(user_val1, user_val2, user_val3, user_val4)
    print(swapped1, swapped2, swapped3, swapped4)
