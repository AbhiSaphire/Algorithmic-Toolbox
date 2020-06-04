def optimal_summands(n):
    summands = []
    i = 1
    while n!=0:
    	if i <= n:
    		summands.append(i)
    		n, i = n-i, i+1
    	else:
    		n += summands.pop()
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')