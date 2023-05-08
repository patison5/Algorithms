# 441. [Easy] Arranging Coins

# На базе формулы суммы арифмитической прогрессии

def arrangeCoins(n: int) -> int:
	return int(math.sqrt(2 * n + 0.25) - 0.5)

# print("hello")
print(arrangeCoins(3))