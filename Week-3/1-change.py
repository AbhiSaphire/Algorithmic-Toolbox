m = int(input())
def change(m):
	money = [10, 5, 1]
	count = 0
	while m:
		for i in range(len(money)):
			if m >= money[i]:
				m -= money[i]
				count += 1
	return count

print(change(m))