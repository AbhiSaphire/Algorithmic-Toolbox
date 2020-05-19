def gcd(a, b):
	while a%b !=0:
		c = a%b
		a, b = b, c
	return b

def lcm(a, b):
	return (a*b)//gcd(a, b)

a, b = [int(x) for x in input().split()]
print(lcm(a, b))