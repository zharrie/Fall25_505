def feet_to_steps(user_feet:float):
    num_steps = user_feet / 2.5
    return int(num_steps)

if __name__ == "__main__":
    user_feet = float(input())
    print(feet_to_steps(user_feet))