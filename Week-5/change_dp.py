money = int(input())
coins = [1, 3, 4]
size = money + 1
minMoney = [0] * size
for i in range(1, money+1):
	minMoney[i] = float('inf')
	for j in range(len(coins)):
		if i >= coins[j]:
			numcoins = minMoney[i - coins[j]]+1
			if numcoins < minMoney[i]:
				minMoney[i] = numcoins
print(minMoney[money])