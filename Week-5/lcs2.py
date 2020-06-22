def common_sub(X, Y, m, n):
    L = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1): 
        for j in range(n+1): 
            if (i == 0 or j == 0): 
                L[i][j] = 0
            elif (X[i-1] == Y[j-1]): 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1], L[i][j]) 
    return L[m][n]


n = int(input())
a1 = [int(x) for x in input().split()][:n]
d = int(input())
a2 = [int(x) for x in input().split()][:d]
print(common_sub(a1, a2, n, d))