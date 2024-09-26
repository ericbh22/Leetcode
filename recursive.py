def fib(n):
    if n == 1:
        return 1 
    if n==0:
        return 0 
    return fib(n-1) + fib(n-2)

print(fib(5))

def fac(n,total=1):
    if n == 1:
        return total
    return fac(n-1,total*n)

print(fac(5))