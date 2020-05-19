def pisanoPeriod(m): 
    a, b = 0, 1
    for i in range(0, m * m): 
        c = (a+b)%m
        a, b = b, c
        if (a == 0 and b == 1): 
            return i + 1

def fib(n, m):
    n = n % pisanoPeriod(m)
    a, b = 0, 1
    if n <= 1:
        return n
    for i in range(n-1):
        c = a + b
        a, b = b, c
    return (b) 


n, m = [int(x) for x in input().split()]
print(fib(n, m)%m)