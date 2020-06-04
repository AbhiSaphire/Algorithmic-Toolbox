def max_dot_product_new(a, b):
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    n = int(input())
    l1 = [int(x) for x in input().split()][:n]
    l2 = [int(x) for x in input().split()][:n]
    print(max_dot_product_new(l1, l2))
