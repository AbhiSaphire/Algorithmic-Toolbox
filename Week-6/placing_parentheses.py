import math

def eval(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def MinAndMax(M, m, i, j, operators):
    min_value = float('inf')
    max_value = float('-inf')
    for k in range(i, j):
        a = eval(M[i][k], M[k+1][j], operators[k])
        b = eval(M[i][k], m[k+1][j], operators[k])
        c = eval(m[i][k], M[k+1][j], operators[k])
        d = eval(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

def get_maximum_value(operands, operators):
    n = len(operands)
    m = [[0 for x in range(n)] for x in range(n)]
    M = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]
    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)
            # for i in range(n):
            #     print(m[i], "      ", M[i])
            # print()
            # print()

    return M[0][n-1]

if __name__ == "__main__":
    expression = input()
    operators, operands = [], []
    for i in expression:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            operands.append(int(i))

    print(get_maximum_value(operands, operators))