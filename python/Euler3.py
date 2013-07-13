import math
data = 600851475143 
number = 600851475143

factor = 2
factors = [1]
while factor < int(math.sqrt(data)):
	if number%factor==0:
		factors.append(factor)
		number = number / factor
	else:
		factor += 1
factors.sort()
factors.reverse()
print factors[0]
