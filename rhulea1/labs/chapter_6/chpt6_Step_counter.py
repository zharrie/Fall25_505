# Define your function here 
def feet_to_steps(user_feet):
# convert feet to steps by using 2.5 feet to 1 step
    steps = user_feet / 2.5
    return int(steps)

#Main program
def main():
    #Read input as a float
    feet_walked = float(input())
    steps_walked = feet_to_steps(feet_walked)

    #Output result
    print(steps_walked)
if __name__ == "__main__":
    main()
