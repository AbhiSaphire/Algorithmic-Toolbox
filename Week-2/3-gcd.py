def gcd(a, b):
	while a%b != 0:
		c = a%b
		a, b = b, c
	return b

a, b = [int(x) for x in input().split()]
print(gcd(a, b))