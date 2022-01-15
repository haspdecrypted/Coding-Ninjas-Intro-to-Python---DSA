def fib_iter(n):
    a=0
    b=1
    for i in range(n):
        total = a + b
        a=b
        b= total
    return a
         
n=int(input())
print(fib_iter(n))