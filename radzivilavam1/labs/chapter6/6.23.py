def fibonacci(n):
    # Type your code here. 
    if n < 0:
        return -1
    
    fib_seq = [0, 1]

    for i in range(0, n):
        total = fib_seq[i] + fib_seq[i+1]
        fib_seq.append(total)

    return fib_seq[n]

if __name__ == "__main__":
    start_num = int(input())

    print(f"fibonacci({start_num}) is {fibonacci(start_num)}")