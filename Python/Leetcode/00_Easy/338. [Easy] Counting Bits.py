# 338. [Easy] Counting Bits

def countBits(n: int) -> list[int]:
    result = []
    for number in range(n + 1):
        amount = 0
        for j in range(31):
            right_bit = (number >> j) & 1
            if right_bit:
                amount += 1
        result.append(amount)
    return result


print(countBits(2))