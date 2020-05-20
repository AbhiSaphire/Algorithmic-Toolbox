def get_optimal_value(capacity, val_wt):
    optimal_value = 0.
    val_wt.sort(key= lambda x: x[0]/x[1], reverse=True)
    for i in val_wt:
    	if capacity == 0:
    		return optimal_value
    	deduce = min(i[1], capacity)
    	optimal_value += deduce*i[0]/i[1]
    	capacity -= deduce
    return optimal_value

if __name__ == "__main__":
	val_wt = []
	n, capacity = [int(x) for x in input().split()]
	if capacity == 0:
		print(0)
	for _ in range(n):
		value, weight = [int(x) for x in input().split()]
		val_wt.append((value, weight))
	opt_value = get_optimal_value(capacity, val_wt)
	print("{:.10f}".format(opt_value))