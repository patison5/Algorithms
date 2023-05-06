# 190. [Easy] Reverse Bits

def reverseBits(n: int) -> int:
	result = 0
	for i in range(32):
		last_bit = (n >> i) & 1
		result = result | (last_bit << (31 - i))
	return result



# 0001 -> 1
# 0010 -> 2
# 0011 -> 3
# 0100 -> 4
# 0101 -> 5
# 0110 -> 6
# 0111 -> 7
# 1000 -> 8
# 1001 -> 9


print(bin(7))
print(bin(reverseBits(7)))


print(8, 8 & 1, bin(8)[2:])
print(7, 7 & 1, bin(7)[2:])
print(6, 6 & 1, bin(6)[2:])
print(4, 4 & 1, bin(4)[2:])
print(3, 3 & 1, bin(3)[2:])
print(2, 2 & 1, bin(2)[2:])
print(1, 1 & 1, bin(1)[2:])
