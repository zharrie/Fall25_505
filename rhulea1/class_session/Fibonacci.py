
def fibonacci(n):   
    a,b = 0,1
    for i in range(n):
        print(a)
        a,b = b, a+b
fib_sequence = fibonacci(5)
print(fib_sequence)
