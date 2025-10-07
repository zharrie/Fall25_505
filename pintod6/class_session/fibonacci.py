def fibonacci(n):
    l = []
    a, b = 0, 1
    l.append(a)
    l.append(b)
    for i in range(n - 2):
        c = a + b 
        a = b
        b = c
        l.append(b)
        
    return l
    
a = fibonacci(5)
print(a)