def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3

if __name__ == "__main__": 
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())

swapped1, swapped2, swapped3, swapped4 = swap_values(val1, val2, val3, val4)

print(swapped1, swapped2, swapped3, swapped4)