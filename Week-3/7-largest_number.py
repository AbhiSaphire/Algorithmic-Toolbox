def isGreaterOrEqual(digit, maxdigit):
	if int(digit+maxdigit) >= int(maxdigit+digit):
		return True
	return False

def largest_number(data):
    res = ""
    while len(data) != 0:
    	maxdigit = 0
    	for digit in data:
    		if isGreaterOrEqual(str(digit), str(maxdigit)):
    			maxdigit = digit
    	res += str(maxdigit)
    	data.remove(maxdigit)
    return res

if __name__ == '__main__':
    n = int(input())
    data = [int(x) for x in input().split()][:n]
    print(largest_number(data))