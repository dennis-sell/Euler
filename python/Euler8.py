import itertools
from numpy import prod

f = open("8.txt", "r")
numbers = []
for line in f:
  numbers.append([int(s) for s in line if s in "1234567890"])
numbers = list(itertools.chain(*numbers))

maxProduct = 0;
for i in range(len(numbers) - 12):
  product = prod(numbers[i:i+13])
  maxProduct = max(maxProduct,product)

print maxProduct
