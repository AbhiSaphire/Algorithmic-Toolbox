def fib(n):
    n = (n+2)%60
    if n==1:
        print(0)
        exit()
    elif n==0:
        print(9)
        exit()
    a,b = 0, 1
    for i in range(2,n+1):
        c = (a+b)%10
        a, b = b, c
    if c!=0:
        print(c-1)
    else:
        print(9)

n = int(input())
if n<=1:
    print(n)  
    exit()
fib(n)