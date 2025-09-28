# Define your function here.
def swap_values(user_val1, user_val2, user_val3, user_val4):
    return (user_val2, user_val1, user_val4, user_val3)


if __name__ == "__main__":
    v1, v2, v3, v4 = swap_values(int(input()), int(input()), int(input()), int(input()))
    
    print(v1, v2, v3, v4, sep=" ")