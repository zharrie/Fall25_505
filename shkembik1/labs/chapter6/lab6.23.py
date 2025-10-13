def fibonacci(n):
   
    if n < 0:
        return -1
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    start_num = int(input())
    print(f"fibonacci({start_num}) is {fibonacci(start_num)}")   