import math
data = 600851475143 
number = 600851475143

factor = 2
while number != 1:
	if number % factor == 0:
		number = number / factor
	else:
		factor += 1
print factor
