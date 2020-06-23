import numpy

def knapsack(W, n, items):
	value = numpy.zeros((W+1, n+1))
	for i in range(1, W+1):
		for j in range(1, n+1):
            # if item i is not part of optimal knapsack
			value[i][j] = value[i][j-1]
			if items[j-1]<=i:
                # if item i is part of optimal knapsack
				temp = value[i-items[j-1]][j-1] + items[j-1]
                # max(i in knapsack, i not in knapsack)
				if temp > value[i][j]:
					value[i][j] = temp

	return (int(value[W][n]))


W, n = input().split()
W, n = int(W), int(n)
weights = [int(x) for x in input().split()][:n]
print(knapsack(W, n, weights))