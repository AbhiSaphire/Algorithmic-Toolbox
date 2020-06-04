def compute_min_refills(distance, tank, stops):
	count = 0
	i = 0
	distCovered = 0
	if stops[i]+tank >= distance:
		return count
	while (i <= n):
		distCovered = i
		while (i < n-1 and (stops[i + 1] - stops[distCovered]) <= tank):
			i += 1
		if (i == distCovered):
			return -1
		count += 1
		if (stops[i] + tank >= distance):
			return count+1
	return -1

def minRefills(n, L, x):
	numRefill = currentRefill = 0
	while currentRefill <= n-1:
		lastRefill = currentRefill
		while currentRefill <= n-1 and x[currentRefill + 1]-x[lastRefill] <= L:
			currentRefill += 1
		if currentRefill == lastRefill:
			return -1
		if currentRefill <= n:
			numRefill += 1
	return numRefill

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [int(x) for x in input().split()][:n]
    print(compute_min_refills(d, m, stops))
    print(minRefills(d, m, stops))