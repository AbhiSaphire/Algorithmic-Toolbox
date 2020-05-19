# # Uses python3
# from sys import stdin

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10

# if __name__ == '__main__':
#     n = int(stdin.read())
#     print(fibonacci_sum_squares_naive(n))



def fib(n):
    a,b = 0, 1
    for i in range(2,n+1):
        c = (a+b)%10
        a, b = b, c
    return c

n = int(input())
if n<=1:
    print(n)  
    exit()

less_than_n = n%60
less_than_n_plus_1 = (n+1)%60

if less_than_n <= 1:
    a = less_than_n
else:
    a = fib(less_than_n)

if less_than_n_plus_1 <= 1:
    b = less_than_n_plus_1
else:
    b = fib(less_than_n_plus_1)

print((a*b)%10)
