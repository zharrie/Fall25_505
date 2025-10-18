def feet_to_steps(user_feet):
    # 1 step = 2.5 feet
    return int(user_feet / 2.5)

if __name__ == "__main__":
   
    feet_walked = float(input())
    print(feet_to_steps(feet_walked))