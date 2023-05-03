# Найти единственный одиночный элемент из набора содержащего по одному дубликату числа
# input: [1,2,1,2,4]
# result: 4
# Решение - взять XOR от каждого элемента

from functools import reduce

list = [1,4,3,2,1,4,3]
print(reduce(lambda x, y: x ^ y, list))
