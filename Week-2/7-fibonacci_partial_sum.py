# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

#     return sum % 10


# from_, to = [int(x) for x in input().split()]
# print(fibonacci_partial_sum_naive(from_, to))

def fib(n):
    a,b = 0, 1
    for i in range(2,n+1):
        c = (a+b)%10
        a, b = b, c
    return (c-1)

m, n = [int(x) for x in input().split()]

if n<=1:
    print(n)  
    exit()

less_than_n = (n+2)%60
less_than_m = (m+1)%60

if less_than_n <= 1:
    a = less_than_n - 1
else:
    a = fib(less_than_n)

if less_than_m <= 1:
    b = less_than_m - 1
else:
    b = fib(less_than_m)

if a >= b:
    print(a - b)
else:
    print(10 + a - b)