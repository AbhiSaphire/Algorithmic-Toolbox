def compute_min_refills(distance, tank, stops):
	rCount = i = currLocation = 0
	refillPos = -2
	stops.append(distance)
	while True:
		if tank + currLocation >= distance:
			return rCount
		if tank < stops[i] - currLocation:
			refillPos = i - 1
			if currLocation == stops[refillPos]:
				return -1
			rCount += 1
			currLocation = stops[i - 1]
			i -= 1
			continue
		i += 1
	return -1

# def minRefills(n, L, x):
# 	numRefill = currentRefill = 0
# 	while currentRefill <= n-1:
# 		lastRefill = currentRefill
# 		while currentRefill <= n-1 and x[currentRefill+1]-x[lastRefill+1] <= L:
# 			currentRefill += 1
# 		if currentRefill == lastRefill:
# 			return -1
# 		if currentRefill <= n:
# 			numRefill += 1
# 	return numRefill

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [int(x) for x in input().split()][:n]
    print(compute_min_refills(d, m, stops))
    # print(minRefills(d, m, stops))