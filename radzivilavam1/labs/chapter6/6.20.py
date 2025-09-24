# Define your function here.
def feet_to_steps(num_of_feet: float):
    num_of_steps = int(num_of_feet / 2.5)
    print(num_of_steps)
    return num_of_steps


if __name__ == "__main__":
    # Type your code here.
    num_of_feet = float(input())

    feet_to_steps(num_of_feet)