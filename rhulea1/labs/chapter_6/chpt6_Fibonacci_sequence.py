def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    #Starting with the first 2 fibonacci numbers
    a, b = 0, 1
    #Compute the nth fibonacci number iteratively
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c 
    return b
if __name__ == "__main__":
    start_num = int(input())
    result = fibonacci(start_num)
    print(f"fibonacci({start_num}) is {fibonacci(start_num)}")