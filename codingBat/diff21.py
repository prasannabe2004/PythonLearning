# Assignments from http://codingbat.com/
# Warmup1

import math

def diff21(n):
	diff = math.fabs(n-21)
	if diff > 21:
		return diff*2
	else:
		return diff

a = diff21(19)

print("result = "+str(a))