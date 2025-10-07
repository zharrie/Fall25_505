n = 5
   
a,b = 0,1  

fib_seq = [0, 1]

for i in range(n):


    total = fib_seq[i] + fib_seq[i+1]
    fib_seq.append(total)

print(fib_seq[:-2])












 

