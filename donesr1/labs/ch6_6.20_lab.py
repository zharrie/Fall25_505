def feet_to_steps(user_feet):
    return int(feet / 2.5)
    if __name__ == "__main__":

feet_walked = float(input())
steps = feet_to_steps(feet_walked)
print(steps)
