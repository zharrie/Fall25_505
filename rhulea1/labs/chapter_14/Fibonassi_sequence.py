def fibonacci(n):
    # Return -1 for negative numbers
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    start_num = int(input())
    print(f"fibonacci({start_num}) is {fibonacci(start_num)}")