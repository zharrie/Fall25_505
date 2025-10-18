def swap_values(user_val1, user_val2, user_val3, user_val4):
    # Swap 1st with 2nd, and 3rd with 4th
    return user_val2, user_val1, user_val4, user_val3

if __name__ == "__main__": 
    # Type your code here. Your code must call the function.
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    w, x, y, z = swap_values(a, b, c, d)
    print(w, x, y, z)